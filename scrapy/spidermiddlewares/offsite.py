"""
Offsite Spider Middleware

See documentation in docs/topics/spider-middleware.rst
"""
import re
import logging
import warnings

from scrapy import signals
from scrapy.http import Request
from scrapy.utils.httpobj import urlparse_cached
from scrapy.crawler import Crawler
from scrapy.http.request import Request
from scrapy.http.response import Response
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.statscollectors import MemoryStatsCollector
from tests.test_engine import AttrsItem
from typing import Any, Dict, Iterator, List, Union

logger = logging.getLogger(__name__)


class OffsiteMiddleware:

    def __init__(self, stats: MemoryStatsCollector) -> None:
        self.stats = stats

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> OffsiteMiddleware:
        o = cls(crawler.stats)
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        return o

    def process_spider_output(self, response: Response, result: Union[Iterator[Any], List[Request]], spider: Spider) -> Iterator[Union[Request, Dict[str, int], Dict[str, List[Union[Any, str]]], Dict[str, List[str]], Dict[str, str], AttrsItem, Item, Dict[Any, Any]]]:
        for x in result:
            if isinstance(x, Request):
                if x.dont_filter or self.should_follow(x, spider):
                    yield x
                else:
                    domain = urlparse_cached(x).hostname
                    if domain and domain not in self.domains_seen:
                        self.domains_seen.add(domain)
                        logger.debug(
                            "Filtered offsite request to %(domain)r: %(request)s",
                            {'domain': domain, 'request': x}, extra={'spider': spider})
                        self.stats.inc_value('offsite/domains', spider=spider)
                    self.stats.inc_value('offsite/filtered', spider=spider)
            else:
                yield x

    def should_follow(self, request: Request, spider: Spider) -> bool:
        regex = self.host_regex
        # hostname can be None for wrong urls (like javascript links)
        host = urlparse_cached(request).hostname or ''
        return bool(regex.search(host))

    def get_host_regex(self, spider):
        """Override this method to implement a different offsite policy"""
        allowed_domains = getattr(spider, 'allowed_domains', None)
        if not allowed_domains:
            return re.compile('')  # allow all by default
        url_pattern = re.compile(r"^https?://.*$")
        port_pattern = re.compile(r":\d+$")
        domains = []
        for domain in allowed_domains:
            if domain is None:
                continue
            elif url_pattern.match(domain):
                message = ("allowed_domains accepts only domains, not URLs. "
                           f"Ignoring URL entry {domain} in allowed_domains.")
                warnings.warn(message, URLWarning)
            elif port_pattern.search(domain):
                message = ("allowed_domains accepts only domains without ports. "
                           f"Ignoring entry {domain} in allowed_domains.")
                warnings.warn(message, PortWarning)
            else:
                domains.append(re.escape(domain))
        regex = fr'^(.*\.)?({"|".join(domains)})$'
        return re.compile(regex)

    def spider_opened(self, spider: Spider) -> None:
        self.host_regex = self.get_host_regex(spider)
        self.domains_seen = set()


class URLWarning(Warning):
    pass


class PortWarning(Warning):
    pass
