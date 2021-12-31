from scrapy.exceptions import StopDownload, _InvalidOutput, NotConfigured
from scrapy.utils.request import request_httprepr
from scrapy.utils.response import response_httprepr
from scrapy.utils.python import global_object_name
from scrapy.core.downloader.handlers.http11 import TunnelError
from scrapy.crawler import Crawler
from scrapy.http.request import Request
from scrapy.http.response import Response
from scrapy.spiders import Spider
from scrapy.statscollectors import MemoryStatsCollector
from tests.test_downloadermiddleware_stats import MyException
from twisted.internet.defer import CancelledError
from twisted.internet.error import ConnectError, DNSLookupError
from twisted.web._newclient import ResponseFailed
from typing import Union


class DownloaderStats:

    def __init__(self, stats: MemoryStatsCollector) -> None:
        self.stats = stats

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> DownloaderStats:
        if not crawler.settings.getbool('DOWNLOADER_STATS'):
            raise NotConfigured
        return cls(crawler.stats)

    def process_request(self, request: Request, spider: Spider) -> None:
        self.stats.inc_value('downloader/request_count', spider=spider)
        self.stats.inc_value(f'downloader/request_method_count/{request.method}', spider=spider)
        reqlen = len(request_httprepr(request))
        self.stats.inc_value('downloader/request_bytes', reqlen, spider=spider)

    def process_response(self, request: Request, response: Response, spider: Spider) -> Response:
        self.stats.inc_value('downloader/response_count', spider=spider)
        self.stats.inc_value(f'downloader/response_status_count/{response.status}', spider=spider)
        reslen = len(response_httprepr(response))
        self.stats.inc_value('downloader/response_bytes', reslen, spider=spider)
        return response

    def process_exception(self, request: Request, exception: Union[MyException, ZeroDivisionError, ResponseFailed, _InvalidOutput, DNSLookupError, CancelledError, StopDownload, ConnectError, TunnelError], spider: Spider) -> None:
        ex_class = global_object_name(exception.__class__)
        self.stats.inc_value('downloader/exception_count', spider=spider)
        self.stats.inc_value(f'downloader/exception_type_count/{ex_class}', spider=spider)
