from scrapy.crawler import Crawler
from scrapy.http.request import Request
from scrapy.settings import Settings
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
from twisted.internet.defer import Deferred
from typing import (
    Optional,
    Tuple,
    Union,
)


def _get_concurrency_delay(
    concurrency: int,
    spider: Union[ItemSpider, NotGeneratorCallbackSpider, NotGeneratorOutputChainSpider, CrawlSpiderWithParseMethod, TestSpider, HeadersReceivedCallbackSpider, SimpleSpider, SingleRequestSpider, GeneratorOutputChainSpider, FollowAllSpider, SignalCatcherSpider, TestSpider, StartUrlsSpider, KeywordArgumentsSpider, _HttpErrorSpider, GeneratorCallbackSpider, BytesReceivedCallbackSpider, DuplicateStartRequestsSpider, ProcessSpiderInputSpiderWithoutErrback, RecoverySpider, DelaySpider, ItemSpider],
    settings: Settings
) -> Tuple[int, float]: ...


class Downloader:
    def __init__(self, crawler: Crawler) -> None: ...
    def _download(
        self,
        slot: Slot,
        request: Request,
        spider: Union[ItemSpider, NotGeneratorCallbackSpider, NotGeneratorOutputChainSpider, CrawlSpiderWithParseMethod, TestSpider, HeadersReceivedCallbackSpider, SingleRequestSpider, SimpleSpider, GeneratorOutputChainSpider, FollowAllSpider, SignalCatcherSpider, TestSpider, StartUrlsSpider, KeywordArgumentsSpider, _HttpErrorSpider, GeneratorCallbackSpider, BytesReceivedCallbackSpider, ProcessSpiderInputSpiderWithoutErrback, DuplicateStartRequestsSpider, RecoverySpider, DelaySpider, ItemSpider]
    ) -> Deferred: ...
    def _enqueue_request(
        self,
        request: Request,
        spider: Union[NotGeneratorOutputChainSpider, NotGeneratorCallbackSpider, ItemSpider, CrawlSpiderWithParseMethod, TestSpider, HeadersReceivedCallbackSpider, SingleRequestSpider, SimpleSpider, FollowAllSpider, SignalCatcherSpider, GeneratorOutputChainSpider, TestSpider, StartUrlsSpider, _HttpErrorSpider, KeywordArgumentsSpider, GeneratorCallbackSpider, BytesReceivedCallbackSpider, DuplicateStartRequestsSpider, ProcessSpiderInputSpiderWithoutErrback, RecoverySpider, DelaySpider, ItemSpider]
    ) -> Deferred: ...
    def _get_slot(
        self,
        request: Request,
        spider: Union[ItemSpider, NotGeneratorCallbackSpider, NotGeneratorOutputChainSpider, CrawlSpiderWithParseMethod, TestSpider, HeadersReceivedCallbackSpider, SingleRequestSpider, SimpleSpider, SignalCatcherSpider, GeneratorOutputChainSpider, FollowAllSpider, TestSpider, StartUrlsSpider, KeywordArgumentsSpider, _HttpErrorSpider, GeneratorCallbackSpider, BytesReceivedCallbackSpider, DuplicateStartRequestsSpider, ProcessSpiderInputSpiderWithoutErrback, DelaySpider, RecoverySpider, ItemSpider]
    ) -> Tuple[str, Slot]: ...
    def _get_slot_key(
        self,
        request: Request,
        spider: Optional[Union[ItemSpider, NotGeneratorCallbackSpider, NotGeneratorOutputChainSpider, CrawlSpiderWithParseMethod, TestSpider, HeadersReceivedCallbackSpider, SingleRequestSpider, SimpleSpider, FollowAllSpider, SignalCatcherSpider, GeneratorOutputChainSpider, TestSpider, StartUrlsSpider, _HttpErrorSpider, KeywordArgumentsSpider, GeneratorCallbackSpider, BytesReceivedCallbackSpider, DuplicateStartRequestsSpider, ProcessSpiderInputSpiderWithoutErrback, DelaySpider, RecoverySpider, ItemSpider]]
    ) -> str: ...
    def _process_queue(
        self,
        spider: Union[ItemSpider, NotGeneratorOutputChainSpider, NotGeneratorCallbackSpider, CrawlSpiderWithParseMethod, TestSpider, HeadersReceivedCallbackSpider, SingleRequestSpider, SimpleSpider, GeneratorOutputChainSpider, FollowAllSpider, SignalCatcherSpider, TestSpider, StartUrlsSpider, KeywordArgumentsSpider, _HttpErrorSpider, GeneratorCallbackSpider, BytesReceivedCallbackSpider, ProcessSpiderInputSpiderWithoutErrback, DuplicateStartRequestsSpider, RecoverySpider, DelaySpider, ItemSpider],
        slot: Slot
    ) -> None: ...
    def _slot_gc(self, age: int = ...) -> None: ...
    def close(self) -> None: ...
    def fetch(
        self,
        request: Request,
        spider: Union[ItemSpider, NotGeneratorCallbackSpider, NotGeneratorOutputChainSpider, CrawlSpiderWithParseMethod, TestSpider, HeadersReceivedCallbackSpider, SimpleSpider, SingleRequestSpider, SignalCatcherSpider, GeneratorOutputChainSpider, FollowAllSpider, TestSpider, StartUrlsSpider, KeywordArgumentsSpider, _HttpErrorSpider, GeneratorCallbackSpider, BytesReceivedCallbackSpider, ProcessSpiderInputSpiderWithoutErrback, DuplicateStartRequestsSpider, RecoverySpider, DelaySpider, ItemSpider]
    ) -> Deferred: ...
    def needs_backout(self) -> bool: ...


class Slot:
    def __init__(self, concurrency: int, delay: float, randomize_delay: bool) -> None: ...
    def __repr__(self) -> str: ...
    def close(self) -> None: ...
    def download_delay(self) -> float: ...
    def free_transfer_slots(self) -> int: ...
