from scrapy.crawler import Crawler
from scrapy.http.request import Request
from scrapy.spiders import Spider
from tests.spiders import (
    BytesReceivedCallbackSpider,
    CrawlSpiderWithParseMethod,
    DelaySpider,
    DuplicateStartRequestsSpider,
    FollowAllSpider,
    HeadersReceivedCallbackSpider,
    SimpleSpider,
    SingleRequestSpider,
)
from tests.test_crawler import NoRequestsSpider
from tests.test_downloadermiddleware_httpauth import (
    TestSpider,
    TestSpiderAny,
    TestSpiderLegacy,
)
from tests.test_engine import TestSpider
from tests.test_pipelines import ItemSpider
from tests.test_request_cb_kwargs import KeywordArgumentsSpider
from tests.test_request_left import SignalCatcherSpider
from tests.test_scheduler import StartUrlsSpider
from tests.test_scheduler_base import TestSpider
from tests.test_signals import ItemSpider
from tests.test_spidermiddleware_httperror import _HttpErrorSpider
from tests.test_spidermiddleware_output_chain import (
    GeneratorCallbackSpider,
    GeneratorOutputChainSpider,
    NotGeneratorCallbackSpider,
    NotGeneratorOutputChainSpider,
    ProcessSpiderInputSpiderWithoutErrback,
    RecoverySpider,
)
from typing import Union


class HttpAuthMiddleware:
    @classmethod
    def from_crawler(cls, crawler: Crawler) -> HttpAuthMiddleware: ...
    def process_request(self, request: Request, spider: Spider) -> None: ...
    def spider_opened(
        self,
        spider: Union[TestSpiderAny, StartUrlsSpider, BytesReceivedCallbackSpider, TestSpiderLegacy, NotGeneratorCallbackSpider, CrawlSpiderWithParseMethod, SingleRequestSpider, SimpleSpider, SignalCatcherSpider, FollowAllSpider, NoRequestsSpider, KeywordArgumentsSpider, TestSpider, TestSpider, ItemSpider, TestSpider, _HttpErrorSpider, HeadersReceivedCallbackSpider, GeneratorCallbackSpider, ItemSpider, NotGeneratorOutputChainSpider, DuplicateStartRequestsSpider, ProcessSpiderInputSpiderWithoutErrback, DelaySpider, RecoverySpider, GeneratorOutputChainSpider]
    ) -> None: ...
