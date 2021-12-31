from scrapy.crawler import Crawler
from scrapy.statscollectors import MemoryStatsCollector
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


class LogStats:
    def __init__(self, stats: MemoryStatsCollector, interval: float = ...) -> None: ...
    @classmethod
    def from_crawler(cls, crawler: Crawler) -> LogStats: ...
    def log(
        self,
        spider: Union[TestSpider, ItemSpider, TestSpider, DuplicateStartRequestsSpider, KeywordArgumentsSpider, DelaySpider, HeadersReceivedCallbackSpider, NoRequestsSpider, SignalCatcherSpider, GeneratorCallbackSpider, NotGeneratorOutputChainSpider, ProcessSpiderInputSpiderWithoutErrback, StartUrlsSpider, RecoverySpider, SingleRequestSpider, SimpleSpider, ItemSpider, GeneratorOutputChainSpider, FollowAllSpider, BytesReceivedCallbackSpider, _HttpErrorSpider, CrawlSpiderWithParseMethod, NotGeneratorCallbackSpider]
    ) -> None: ...
    def spider_closed(
        self,
        spider: Union[TestSpider, ItemSpider, TestSpider, DuplicateStartRequestsSpider, KeywordArgumentsSpider, DelaySpider, HeadersReceivedCallbackSpider, NoRequestsSpider, SignalCatcherSpider, GeneratorCallbackSpider, NotGeneratorOutputChainSpider, ProcessSpiderInputSpiderWithoutErrback, StartUrlsSpider, RecoverySpider, SingleRequestSpider, SimpleSpider, ItemSpider, GeneratorOutputChainSpider, FollowAllSpider, BytesReceivedCallbackSpider, _HttpErrorSpider, CrawlSpiderWithParseMethod, NotGeneratorCallbackSpider],
        reason: str
    ) -> None: ...
    def spider_opened(
        self,
        spider: Union[TestSpider, ItemSpider, TestSpider, DuplicateStartRequestsSpider, KeywordArgumentsSpider, DelaySpider, HeadersReceivedCallbackSpider, NoRequestsSpider, SignalCatcherSpider, GeneratorCallbackSpider, NotGeneratorOutputChainSpider, ProcessSpiderInputSpiderWithoutErrback, StartUrlsSpider, RecoverySpider, SingleRequestSpider, SimpleSpider, ItemSpider, GeneratorOutputChainSpider, FollowAllSpider, BytesReceivedCallbackSpider, _HttpErrorSpider, CrawlSpiderWithParseMethod, NotGeneratorCallbackSpider]
    ) -> None: ...
