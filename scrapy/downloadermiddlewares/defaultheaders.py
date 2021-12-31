"""
DefaultHeaders downloader middleware

See documentation in docs/topics/downloader-middleware.rst
"""

from scrapy.utils.python import without_none_values
from scrapy.crawler import Crawler
from scrapy.http.request import Request
from scrapy.spiders import Spider


class DefaultHeadersMiddleware:

    def __init__(self, headers):
        self._headers = headers

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> DefaultHeadersMiddleware:
        headers = without_none_values(crawler.settings['DEFAULT_REQUEST_HEADERS'])
        return cls(headers.items())

    def process_request(self, request: Request, spider: Spider) -> None:
        for k, v in self._headers:
            request.headers.setdefault(k, v)
