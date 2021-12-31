from scrapy.core.downloader.handlers.datauri import DataURIDownloadHandler
from scrapy.core.downloader.handlers.file import FileDownloadHandler
from scrapy.core.downloader.handlers.ftp import FTPDownloadHandler
from scrapy.core.downloader.handlers.http11 import HTTP11DownloadHandler
from scrapy.crawler import Crawler
from scrapy.http.request import Request
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
from tests.test_downloader_handlers import (
    DummyDH,
    DummyLazyDH,
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
from twisted.internet.defer import (
    Deferred,
    DeferredList,
)
from typing import (
    Iterator,
    Optional,
    Union,
)


class DownloadHandlers:
    def __init__(self, crawler: Crawler) -> None: ...
    def _close(self, *_a, **_kw) -> Iterator[DeferredList]: ...
    def _get_handler(
        self,
        scheme: str
    ) -> Optional[Union[DummyLazyDH, DataURIDownloadHandler, HTTP11DownloadHandler]]: ...
    def _load_handler(
        self,
        scheme: str,
        skip_lazy: bool = ...
    ) -> Optional[Union[FTPDownloadHandler, HTTP11DownloadHandler, DummyLazyDH, DummyDH, FileDownloadHandler, DataURIDownloadHandler]]: ...
    def download_request(
        self,
        request: Request,
        spider: Union[DelaySpider, DuplicateStartRequestsSpider, ItemSpider, _HttpErrorSpider, GeneratorCallbackSpider, TestSpider, TestSpider, HeadersReceivedCallbackSpider, ProcessSpiderInputSpiderWithoutErrback, RecoverySpider, SimpleSpider, FollowAllSpider, StartUrlsSpider, SingleRequestSpider, KeywordArgumentsSpider, BytesReceivedCallbackSpider, NotGeneratorOutputChainSpider, NotGeneratorCallbackSpider, CrawlSpiderWithParseMethod, ItemSpider, SignalCatcherSpider, GeneratorOutputChainSpider]
    ) -> Deferred: ...
