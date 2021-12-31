from scrapy.core.engine import ExecutionEngine
from scrapy.settings import Settings
from scrapy.spiderloader import SpiderLoader
from scrapy.spiders import Spider
from scrapy.utils.spider import DefaultSpider
from tests.spiders import (
    AsyncDefAsyncioGenComplexSpider,
    AsyncDefAsyncioGenLoopSpider,
    AsyncDefAsyncioGenSpider,
    AsyncDefAsyncioReqsReturnSpider,
    AsyncDefAsyncioReturnSingleElementSpider,
    AsyncDefAsyncioReturnSpider,
    AsyncDefAsyncioSpider,
    AsyncDefSpider,
    BrokenStartRequestsSpider,
    BytesReceivedCallbackSpider,
    BytesReceivedErrbackSpider,
    CrawlSpiderWithErrback,
    CrawlSpiderWithParseMethod,
    DelaySpider,
    DuplicateStartRequestsSpider,
    ErrorSpider,
    FollowAllSpider,
    HeadersReceivedCallbackSpider,
    HeadersReceivedErrbackSpider,
    ItemSpider,
    SimpleSpider,
    SingleRequestSpider,
)
from tests.test_crawler import (
    ExceptionSpider,
    NoRequestsSpider,
)
from tests.test_downloader_handlers import (
    DummyDH,
    DummyLazyDH,
    OffDH,
)
from tests.test_dupefilters import (
    DirectDupeFilter,
    FromCrawlerRFPDupeFilter,
    FromSettingsRFPDupeFilter,
)
from tests.test_engine import (
    AttrsItemsSpider,
    ChangeCloseReasonSpider,
    DataClassItemsSpider,
    DictItemsSpider,
    ItemZeroDivisionErrorSpider,
    TestDupeFilterSpider,
    TestSpider,
)
from tests.test_feedexport import (
    FTPFeedStorageWithoutFeedOptions,
    FTPFeedStorageWithoutFeedOptionsWithFromCrawler,
    FileFeedStorageWithoutFeedOptions,
    S3FeedStorageWithoutFeedOptions,
    S3FeedStorageWithoutFeedOptionsWithFromCrawler,
    StdoutFeedStorageWithoutFeedOptions,
)
from tests.test_logformatter import (
    DropSomeItemsPipeline,
    SkipMessagesLogFormatter,
)
from tests.test_pipeline_crawl import (
    BrokenLinksMediaDownloadSpider,
    MediaDownloadSpider,
    RedirectedMediaDownloadSpider,
)
from tests.test_pipelines import (
    AsyncDefAsyncioPipeline,
    AsyncDefNotAsyncioPipeline,
    AsyncDefPipeline,
    DeferredPipeline,
    ItemSpider,
    SimplePipeline,
)
from tests.test_request_attribute_binding import (
    AlternativeCallbacksMiddleware,
    AlternativeCallbacksSpider,
    CatchExceptionDoNotOverrideRequestMiddleware,
    CatchExceptionOverrideRequestMiddleware,
    ProcessResponseMiddleware,
    RaiseExceptionRequestMiddleware,
)
from tests.test_request_cb_kwargs import KeywordArgumentsSpider
from tests.test_request_left import SignalCatcherSpider
from tests.test_scheduler import StartUrlsSpider
from tests.test_scheduler_base import (
    MinimalScheduler,
    SimpleScheduler,
    TestSpider,
)
from tests.test_signals import ItemSpider
from tests.test_spiderloader.test_spiders.spider1 import Spider1
from tests.test_spidermiddleware_httperror import _HttpErrorSpider
from tests.test_spidermiddleware_output_chain import (
    GeneratorCallbackSpider,
    GeneratorCallbackSpiderMiddlewareRightAfterSpider,
    GeneratorOutputChainSpider,
    NotGeneratorCallbackSpider,
    NotGeneratorCallbackSpiderMiddlewareRightAfterSpider,
    NotGeneratorOutputChainSpider,
    ProcessSpiderInputSpiderWithErrback,
    ProcessSpiderInputSpiderWithoutErrback,
    RecoverySpider,
)
from twisted.internet.defer import (
    Deferred,
    DeferredList,
)
from typing import (
    Any,
    Dict,
    Iterator,
    List,
    Optional,
    Type,
    Union,
)


class Crawler:
    def __init__(
        self,
        spidercls: Union[Type[NoRequestsSpider], Type[SingleRequestSpider], Type[HeadersReceivedErrbackSpider], Type[DataClassItemsSpider], Type[ItemSpider], Type[SignalCatcherSpider], Type[ChangeCloseReasonSpider], Type[AsyncDefAsyncioGenSpider], Type[NotGeneratorCallbackSpider], Type[AsyncDefAsyncioGenLoopSpider], Type[HeadersReceivedCallbackSpider], Type[AsyncDefAsyncioGenComplexSpider], Type[AsyncDefAsyncioReturnSpider], Type[BytesReceivedCallbackSpider], Type[Spider1], Type[AsyncDefAsyncioReqsReturnSpider], Type[BytesReceivedErrbackSpider], Type[GeneratorCallbackSpiderMiddlewareRightAfterSpider], Type[NotGeneratorOutputChainSpider], Type[AsyncDefAsyncioSpider], Type[CrawlSpiderWithErrback], DefaultSpider, Type[TestSpider], Type[AsyncDefAsyncioReturnSingleElementSpider], Type[StartUrlsSpider], Type[DelaySpider], Type[KeywordArgumentsSpider], Type[GeneratorOutputChainSpider], Type[AttrsItemsSpider], Type[DictItemsSpider], Type[GeneratorCallbackSpider], Type[TestSpider], Type[AsyncDefSpider], Type[DefaultSpider], Type[ProcessSpiderInputSpiderWithoutErrback], Type[FollowAllSpider], Type[ItemSpider], Type[TestDupeFilterSpider], Type[Spider], Type[ItemSpider], Type[ProcessSpiderInputSpiderWithErrback], Type[SimpleSpider], Type[RedirectedMediaDownloadSpider], Type[DuplicateStartRequestsSpider], Type[_HttpErrorSpider], Type[BrokenStartRequestsSpider], Type[RecoverySpider], Type[ItemZeroDivisionErrorSpider], Type[CrawlSpiderWithParseMethod], Type[AlternativeCallbacksSpider], Type[ErrorSpider], Type[ExceptionSpider], Type[NotGeneratorCallbackSpiderMiddlewareRightAfterSpider], Type[MediaDownloadSpider], Type[BrokenLinksMediaDownloadSpider]],
        settings: Optional[Union[Dict[str, str], Dict[str, Union[bool, str]], Dict[str, Union[str, int]], Settings, Dict[str, Optional[Union[bool, str]]]]] = ...
    ) -> None: ...
    def _create_engine(self) -> ExecutionEngine: ...
    def _create_spider(self, *args, **kwargs) -> Spider: ...
    def crawl(self, *args, **kwargs) -> Iterator[Deferred]: ...
    def stop(self) -> Iterator[Deferred]: ...


class CrawlerProcess:
    def __init__(
        self,
        settings: Optional[Union[Dict[str, str], Dict[str, None]]] = ...,
        install_root_handler: bool = ...
    ) -> None: ...
    def _handle_twisted_reactor(self) -> None: ...


class CrawlerRunner:
    def __init__(
        self,
        settings: Optional[Union[Dict[str, Type[DirectDupeFilter]], Dict[str, Dict[Union[Type[RaiseExceptionRequestMiddleware], Type[CatchExceptionOverrideRequestMiddleware]], int]], Dict[str, Type[MinimalScheduler]], Dict[str, Dict[str, Type[OffDH]]], Dict[str, Union[str, Dict[str, Type[FTPFeedStorageWithoutFeedOptionsWithFromCrawler]]]], Dict[str, Union[str, Dict[Type[DropSomeItemsPipeline], int], Type[SkipMessagesLogFormatter]]], Dict[str, Dict[Type[DeferredPipeline], int]], Dict[str, Dict[str, Type[DummyDH]]], Dict[str, Dict[Union[Type[RaiseExceptionRequestMiddleware], Type[CatchExceptionDoNotOverrideRequestMiddleware]], int]], Dict[str, str], Dict[str, Union[bool, Type[FromSettingsRFPDupeFilter]]], Dict[str, Union[str, Dict[str, Dict[str, str]]]], Dict[Any, Any], Dict[str, List[str]], Dict[str, Dict[Type[AsyncDefAsyncioPipeline], int]], Dict[str, Dict[str, Dict[str, str]]], Settings, Dict[str, Dict[str, Dict[Any, Any]]], Dict[str, Union[float, bool]], Dict[str, Dict[str, None]], Dict[str, Dict[Type[AsyncDefPipeline], int]], Dict[str, Union[str, Dict[str, Type[FTPFeedStorageWithoutFeedOptions]]]], Dict[str, Union[str, Dict[str, Type[FileFeedStorageWithoutFeedOptions]]]], Dict[str, Union[Dict[str, Dict[str, str]], int]], Dict[str, Dict[Type[ProcessResponseMiddleware], int]], Dict[str, Union[str, Dict[str, Type[S3FeedStorageWithoutFeedOptionsWithFromCrawler]]]], Dict[str, Dict[str, str]], Dict[str, Dict[Any, Any]], Dict[str, float], Dict[str, Union[str, Dict[Type[DropSomeItemsPipeline], int]]], Dict[str, bool], Dict[str, Type[SimpleScheduler]], Dict[str, Union[str, Dict[str, Type[S3FeedStorageWithoutFeedOptions]]]], Dict[str, Dict[Type[SimplePipeline], int]], Dict[str, Dict[str, Type[DummyLazyDH]]], Dict[str, Union[bool, Type[FromCrawlerRFPDupeFilter]]], Dict[str, Union[Dict[str, int], str]], Dict[str, Optional[str]], Dict[str, Union[Dict[str, int], str, bool]], Dict[str, Dict[Type[AsyncDefNotAsyncioPipeline], int]], Dict[str, Dict[Type[AlternativeCallbacksMiddleware], int]], Dict[str, Union[str, Dict[str, Type[StdoutFeedStorageWithoutFeedOptions]]]], Dict[str, Dict[Type[RaiseExceptionRequestMiddleware], int]], Dict[str, None], Dict[str, Dict[str, int]], Dict[str, int]]] = ...
    ) -> None: ...
    def _crawl(self, crawler: Crawler, *args, **kwargs) -> Deferred: ...
    def _create_crawler(
        self,
        spidercls: Union[Type[NoRequestsSpider], Type[SingleRequestSpider], Type[ItemSpider], Type[DataClassItemsSpider], Type[HeadersReceivedErrbackSpider], Type[SignalCatcherSpider], Type[ChangeCloseReasonSpider], Type[AsyncDefAsyncioGenSpider], Type[NotGeneratorCallbackSpider], Type[AsyncDefAsyncioGenLoopSpider], Type[AsyncDefAsyncioGenComplexSpider], Type[HeadersReceivedCallbackSpider], Type[AsyncDefAsyncioReturnSpider], Type[ExceptionSpider], Type[BytesReceivedCallbackSpider], Type[AsyncDefAsyncioReqsReturnSpider], Type[BytesReceivedErrbackSpider], Type[NotGeneratorOutputChainSpider], Type[GeneratorCallbackSpiderMiddlewareRightAfterSpider], Type[AsyncDefAsyncioSpider], Type[CrawlSpiderWithErrback], Type[TestSpider], Type[AsyncDefAsyncioReturnSingleElementSpider], Type[StartUrlsSpider], Type[DelaySpider], Type[KeywordArgumentsSpider], Type[DictItemsSpider], Type[TestSpider], Type[AttrsItemsSpider], Type[GeneratorCallbackSpider], Type[GeneratorOutputChainSpider], Type[AsyncDefSpider], str, Type[ProcessSpiderInputSpiderWithoutErrback], Type[FollowAllSpider], Type[ItemSpider], Type[TestDupeFilterSpider], Type[Spider], Type[ItemSpider], Type[ProcessSpiderInputSpiderWithErrback], Type[SimpleSpider], Type[RedirectedMediaDownloadSpider], Type[DuplicateStartRequestsSpider], Type[_HttpErrorSpider], Type[CrawlSpiderWithParseMethod], Type[RecoverySpider], Type[ItemZeroDivisionErrorSpider], Type[AlternativeCallbacksSpider], Type[ErrorSpider], Type[BrokenStartRequestsSpider], Type[NotGeneratorCallbackSpiderMiddlewareRightAfterSpider], Type[MediaDownloadSpider], Type[BrokenLinksMediaDownloadSpider]]
    ) -> Crawler: ...
    @staticmethod
    def _get_spider_loader(settings: Settings) -> SpiderLoader: ...
    def _handle_twisted_reactor(self) -> None: ...
    def crawl(
        self,
        crawler_or_spidercls: Union[Type[NoRequestsSpider], Type[SimpleSpider], Type[TestSpider], Crawler, Type[CrawlSpiderWithParseMethod], Type[AsyncDefSpider], Type[AsyncDefAsyncioSpider], Type[ExceptionSpider], Type[CrawlSpiderWithErrback]],
        *args,
        **kwargs
    ) -> Deferred: ...
    def create_crawler(
        self,
        crawler_or_spidercls: Union[Type[SingleRequestSpider], Type[NoRequestsSpider], Type[ItemSpider], Type[HeadersReceivedErrbackSpider], Type[DataClassItemsSpider], Type[SignalCatcherSpider], Type[ChangeCloseReasonSpider], Type[AsyncDefAsyncioGenSpider], Type[NotGeneratorCallbackSpider], Type[AsyncDefAsyncioGenLoopSpider], Type[HeadersReceivedCallbackSpider], Type[AsyncDefAsyncioGenComplexSpider], Type[AsyncDefAsyncioReturnSpider], Type[BytesReceivedCallbackSpider], Type[AsyncDefAsyncioReqsReturnSpider], Crawler, Type[BytesReceivedErrbackSpider], Type[GeneratorCallbackSpiderMiddlewareRightAfterSpider], Type[NotGeneratorOutputChainSpider], Type[AsyncDefAsyncioSpider], Type[CrawlSpiderWithErrback], Type[TestSpider], Type[AsyncDefAsyncioReturnSingleElementSpider], Type[StartUrlsSpider], Type[DelaySpider], Type[KeywordArgumentsSpider], Type[GeneratorOutputChainSpider], Type[AttrsItemsSpider], Type[TestSpider], Type[GeneratorCallbackSpider], Type[DictItemsSpider], Type[AsyncDefSpider], str, Type[ProcessSpiderInputSpiderWithoutErrback], Type[FollowAllSpider], Type[ItemSpider], Type[Spider], Type[TestDupeFilterSpider], Type[ProcessSpiderInputSpiderWithErrback], Type[ItemSpider], Type[SimpleSpider], Type[RedirectedMediaDownloadSpider], Type[DuplicateStartRequestsSpider], Type[_HttpErrorSpider], Type[CrawlSpiderWithParseMethod], Type[RecoverySpider], Type[ItemZeroDivisionErrorSpider], Type[BrokenStartRequestsSpider], Type[AlternativeCallbacksSpider], Type[ErrorSpider], Type[ExceptionSpider], Type[NotGeneratorCallbackSpiderMiddlewareRightAfterSpider], Type[MediaDownloadSpider], Type[BrokenLinksMediaDownloadSpider]]
    ) -> Crawler: ...
    def join(self) -> Iterator[DeferredList]: ...
    @property
    def spiders(self) -> SpiderLoader: ...
