"""
Url Length Spider Middleware

See documentation in docs/topics/spider-middleware.rst
"""

import logging

from scrapy.http import Request
from scrapy.exceptions import NotConfigured
from scrapy.http.request import Request
from scrapy.http.response import Response
from scrapy.settings import Settings
from scrapy.spiders import Spider
from typing import Any, Iterator, List, Union

logger = logging.getLogger(__name__)


class UrlLengthMiddleware:

    def __init__(self, maxlength: int) -> None:
        self.maxlength = maxlength

    @classmethod
    def from_settings(cls, settings: Settings) -> UrlLengthMiddleware:
        maxlength = settings.getint('URLLENGTH_LIMIT')
        if not maxlength:
            raise NotConfigured
        return cls(maxlength)

    def process_spider_output(self, response: Response, result: Union[List[Request], Iterator[Any]], spider: Spider) -> Iterator[Any]:
        def _filter(request):
            if isinstance(request, Request) and len(request.url) > self.maxlength:
                logger.info(
                    "Ignoring link (url length > %(maxlength)d): %(url)s ",
                    {'maxlength': self.maxlength, 'url': request.url},
                    extra={'spider': spider}
                )
                spider.crawler.stats.inc_value('urllength/request_ignored_count', spider=spider)
                return False
            else:
                return True

        return (r for r in result or () if _filter(r))
