"""
Download timeout middleware

See documentation in docs/topics/downloader-middleware.rst
"""

from scrapy import signals
from scrapy.crawler import Crawler
from scrapy.http.request import Request
from scrapy.spiders import Spider


class DownloadTimeoutMiddleware:

    def __init__(self, timeout: float=180) -> None:
        self._timeout = timeout

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> DownloadTimeoutMiddleware:
        o = cls(crawler.settings.getfloat('DOWNLOAD_TIMEOUT'))
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        return o

    def spider_opened(self, spider: Spider) -> None:
        self._timeout = getattr(spider, 'download_timeout', self._timeout)

    def process_request(self, request: Request, spider: Spider) -> None:
        if self._timeout:
            request.meta.setdefault('download_timeout', self._timeout)
