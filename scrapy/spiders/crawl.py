"""
This modules implements the CrawlSpider which is the recommended spider to use
for scraping typical web sites that requires crawling pages.

See documentation in docs/topics/spiders.rst
"""

import copy
from typing import Any, Callable, Dict, Iterator, List, Optional, Tuple, Union, Sequence

from scrapy.http import Request, HtmlResponse
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Spider
from scrapy.utils.spider import iterate_spider_output
from scrapy.crawler import Crawler
from scrapy.http.request import Request
from scrapy.http.response.html import HtmlResponse
from scrapy.http.response.text import TextResponse
from scrapy.link import Link
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from tests.spiders import CrawlSpiderWithParseMethod
from twisted.python.failure import Failure


def _identity(x: List[Link]) -> List[Link]:
    return x


def _identity_process_request(request: Request, response: HtmlResponse) -> Request:
    return request


def _get_method(method: Optional[Union[str, Callable]], spider: CrawlSpiderWithParseMethod) -> Optional[Callable]:
    if callable(method):
        return method
    elif isinstance(method, str):
        return getattr(spider, method, None)


_default_link_extractor = LinkExtractor()


class Rule:

    def __init__(
        self,
        link_extractor: Optional[LxmlLinkExtractor]=None,
        callback: Optional[str]=None,
        cb_kwargs: None=None,
        follow: Optional[bool]=None,
        process_links: Optional[str]=None,
        process_request: Optional[Union[Callable, str]]=None,
        errback: Optional[str]=None,
    ) -> None:
        self.link_extractor = link_extractor or _default_link_extractor
        self.callback = callback
        self.errback = errback
        self.cb_kwargs = cb_kwargs or {}
        self.process_links = process_links or _identity
        self.process_request = process_request or _identity_process_request
        self.follow = follow if follow is not None else not callback

    def _compile(self, spider: CrawlSpiderWithParseMethod) -> None:
        self.callback = _get_method(self.callback, spider)
        self.errback = _get_method(self.errback, spider)
        self.process_links = _get_method(self.process_links, spider)
        self.process_request = _get_method(self.process_request, spider)


class CrawlSpider(Spider):

    rules: Sequence[Rule] = ()

    def __init__(self, *a, **kw) -> None:
        super().__init__(*a, **kw)
        self._compile_rules()

    def _parse(self, response: HtmlResponse, **kwargs) -> Iterator[Any]:
        return self._parse_response(
            response=response,
            callback=self.parse_start_url,
            cb_kwargs=kwargs,
            follow=True,
        )

    def parse_start_url(self, response: HtmlResponse, **kwargs) -> List[Any]:
        return []

    def process_results(self, response: TextResponse, results: Union[Iterator[Any], Tuple[()]]) -> Union[Iterator[Any], Tuple[()]]:
        return results

    def _build_request(self, rule_index: int, link: Link) -> Request:
        return Request(
            url=link.url,
            callback=self._callback,
            errback=self._errback,
            meta=dict(rule=rule_index, link_text=link.text),
        )

    def _requests_to_follow(self, response: TextResponse) -> Iterator[Request]:
        if not isinstance(response, HtmlResponse):
            return
        seen = set()
        for rule_index, rule in enumerate(self._rules):
            links = [lnk for lnk in rule.link_extractor.extract_links(response)
                     if lnk not in seen]
            for link in rule.process_links(links):
                seen.add(link)
                request = self._build_request(rule_index, link)
                yield rule.process_request(request, response)

    def _callback(self, response: TextResponse) -> Iterator[Any]:
        rule = self._rules[response.meta['rule']]
        return self._parse_response(response, rule.callback, rule.cb_kwargs, rule.follow)

    def _errback(self, failure: Failure) -> Iterator[Any]:
        rule = self._rules[failure.request.meta['rule']]
        return self._handle_failure(failure, rule.errback)

    def _parse_response(self, response: TextResponse, callback: Callable, cb_kwargs: Dict[Any, Any], follow: bool=True) -> Iterator[Request]:
        if callback:
            cb_res = callback(response, **cb_kwargs) or ()
            cb_res = self.process_results(response, cb_res)
            for request_or_item in iterate_spider_output(cb_res):
                yield request_or_item

        if follow and self._follow_links:
            for request_or_item in self._requests_to_follow(response):
                yield request_or_item

    def _handle_failure(self, failure: Failure, errback: Callable) -> None:
        if errback:
            results = errback(failure) or ()
            for request_or_item in iterate_spider_output(results):
                yield request_or_item

    def _compile_rules(self) -> None:
        self._rules = []
        for rule in self.rules:
            self._rules.append(copy.copy(rule))
            self._rules[-1]._compile(self)

    @classmethod
    def from_crawler(cls, crawler: Crawler, *args, **kwargs) -> CrawlSpider:
        spider = super().from_crawler(crawler, *args, **kwargs)
        spider._follow_links = crawler.settings.getbool('CRAWLSPIDER_FOLLOW_LINKS', True)
        return spider
