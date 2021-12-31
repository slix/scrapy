"""
This is a middleware to respect robots.txt policies. To activate it you must
enable this middleware and enable the ROBOTSTXT_OBEY setting.

"""

import logging

from twisted.internet.defer import Deferred, maybeDeferred
from scrapy.exceptions import NotConfigured, IgnoreRequest
from scrapy.http import Request
from scrapy.utils.httpobj import urlparse_cached
from scrapy.utils.log import failure_to_exc_info
from scrapy.utils.misc import load_object
from scrapy.crawler import Crawler
from scrapy.http.request import Request
from scrapy.http.response import Response
from scrapy.robotstxt import ProtegoRobotParser, ReppyRobotParser, RerpRobotParser
from twisted.python.failure import Failure
from typing import Optional, Union
from unittest.mock import MagicMock

logger = logging.getLogger(__name__)


class RobotsTxtMiddleware:
    DOWNLOAD_PRIORITY = 1000

    def __init__(self, crawler: Union[MagicMock, Crawler]) -> None:
        if not crawler.settings.getbool('ROBOTSTXT_OBEY'):
            raise NotConfigured
        self._default_useragent = crawler.settings.get('USER_AGENT', 'Scrapy')
        self._robotstxt_useragent = crawler.settings.get('ROBOTSTXT_USER_AGENT', None)
        self.crawler = crawler
        self._parsers = {}
        self._parserimpl = load_object(crawler.settings.get('ROBOTSTXT_PARSER'))

        # check if parser dependencies are met, this should throw an error otherwise.
        self._parserimpl.from_crawler(self.crawler, b'')

    @classmethod
    def from_crawler(cls, crawler: Crawler):
        return cls(crawler)

    def process_request(self, request: Request, spider: None) -> Optional[Deferred]:
        if request.meta.get('dont_obey_robotstxt'):
            return
        d = maybeDeferred(self.robot_parser, request, spider)
        d.addCallback(self.process_request_2, request, spider)
        return d

    def process_request_2(self, rp: Optional[Union[MagicMock, ProtegoRobotParser, ReppyRobotParser, RerpRobotParser]], request: Request, spider: None) -> None:
        if rp is None:
            return

        useragent = self._robotstxt_useragent
        if not useragent:
            useragent = request.headers.get(b'User-Agent', self._default_useragent)
        if not rp.allowed(request.url, useragent):
            logger.debug("Forbidden by robots.txt: %(request)s",
                         {'request': request}, extra={'spider': spider})
            self.crawler.stats.inc_value('robotstxt/forbidden')
            raise IgnoreRequest("Forbidden by robots.txt")

    def robot_parser(self, request: Request, spider: None) -> Optional[Union[Deferred, ProtegoRobotParser, ReppyRobotParser, RerpRobotParser]]:
        url = urlparse_cached(request)
        netloc = url.netloc

        if netloc not in self._parsers:
            self._parsers[netloc] = Deferred()
            robotsurl = f"{url.scheme}://{url.netloc}/robots.txt"
            robotsreq = Request(
                robotsurl,
                priority=self.DOWNLOAD_PRIORITY,
                meta={'dont_obey_robotstxt': True}
            )
            dfd = self.crawler.engine.download(robotsreq)
            dfd.addCallback(self._parse_robots, netloc, spider)
            dfd.addErrback(self._logerror, robotsreq, spider)
            dfd.addErrback(self._robots_error, netloc)
            self.crawler.stats.inc_value('robotstxt/request_count')

        if isinstance(self._parsers[netloc], Deferred):
            d = Deferred()

            def cb(result):
                d.callback(result)
                return result
            self._parsers[netloc].addCallback(cb)
            return d
        else:
            return self._parsers[netloc]

    def _logerror(self, failure: Failure, request: Request, spider: None) -> Failure:
        if failure.type is not IgnoreRequest:
            logger.error("Error downloading %(request)s: %(f_exception)s",
                         {'request': request, 'f_exception': failure.value},
                         exc_info=failure_to_exc_info(failure),
                         extra={'spider': spider})
        return failure

    def _parse_robots(self, response: Response, netloc: str, spider: None) -> None:
        self.crawler.stats.inc_value('robotstxt/response_count')
        self.crawler.stats.inc_value(f'robotstxt/response_status_count/{response.status}')
        rp = self._parserimpl.from_crawler(self.crawler, response.body)
        rp_dfd = self._parsers[netloc]
        self._parsers[netloc] = rp
        rp_dfd.callback(rp)

    def _robots_error(self, failure: Failure, netloc: str) -> None:
        if failure.type is not IgnoreRequest:
            key = f'robotstxt/exception_count/{failure.type}'
            self.crawler.stats.inc_value(key)
        rp_dfd = self._parsers[netloc]
        self._parsers[netloc] = None
        rp_dfd.callback(None)
