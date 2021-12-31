from io import (
    BufferedWriter,
    BytesIO,
    FileIO,
)
from scrapy.crawler import Crawler
from scrapy.exporters import (
    CsvItemExporter,
    JsonItemExporter,
    JsonLinesItemExporter,
    MarshalItemExporter,
    PickleItemExporter,
    XmlItemExporter,
)
from scrapy.extensions.postprocessing import PostProcessingManager
from scrapy.item import Item
from scrapy.spiders import Spider
from tempfile import _TemporaryFileWrapper
from tests.spiders import ItemSpider
from tests.test_feedexport import (
    DummyBlockingFeedStorage,
    FTPFeedStorageWithoutFeedOptions,
    FTPFeedStorageWithoutFeedOptionsWithFromCrawler,
    FailingBlockingFeedStorage,
    FeedPostProcessedExportsTest,
    FileFeedStorageWithoutFeedOptions,
    FromCrawlerCsvItemExporter,
    FromCrawlerFileFeedStorage,
    LogOnStoreFileStorage,
    S3FeedStorageWithoutFeedOptions,
    S3FeedStorageWithoutFeedOptionsWithFromCrawler,
    StdoutFeedStorageWithoutFeedOptions,
)
from twisted.internet.defer import (
    Deferred,
    DeferredList,
)
from twisted.python.failure import Failure
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Type,
    Union,
)
from unittest.mock import (
    MagicMock,
    Mock,
)


def build_storage(
    builder: Union[Type[FTPFeedStorage], Type[DummyBlockingFeedStorage], Type[FTPFeedStorageWithoutFeedOptionsWithFromCrawler], Type[FTPFeedStorageWithoutFeedOptions], Type[FileFeedStorageWithoutFeedOptions], Type[StdoutFeedStorage], Type[FileFeedStorage], Type[S3FeedStorage], Type[StdoutFeedStorageWithoutFeedOptions], Callable, Type[S3FeedStorageWithoutFeedOptionsWithFromCrawler], Type[LogOnStoreFileStorage], Type[FailingBlockingFeedStorage], Type[S3FeedStorageWithoutFeedOptions]],
    uri: str,
    *args,
    feed_options = ...,
    preargs = ...,
    **kwargs
) -> Union[DummyBlockingFeedStorage, FileFeedStorage, FTPFeedStorage, LogOnStoreFileStorage, StdoutFeedStorage, S3FeedStorage]: ...


class BlockingFeedStorage:
    def open(self, spider: Spider) -> _TemporaryFileWrapper: ...
    def store(
        self,
        file: Union[Mock, BytesIO, _TemporaryFileWrapper]
    ) -> Deferred: ...


class FTPFeedStorage:
    def __init__(self, uri: str, use_active_mode: Union[bool, Dict[Any, Any]] = ..., *, feed_options = ...) -> None: ...
    @classmethod
    def from_crawler(
        cls,
        crawler: Crawler,
        uri: str,
        *,
        feed_options = ...
    ) -> FTPFeedStorage: ...


class FeedExporter:
    def __init__(self, crawler: Crawler) -> None: ...
    def _close_slot(
        self,
        slot: _FeedSlot,
        spider: ItemSpider
    ) -> Deferred: ...
    def _exporter_supported(self, format: str) -> Optional[bool]: ...
    def _get_exporter(
        self,
        file: Union[PostProcessingManager, BufferedWriter, _TemporaryFileWrapper, FileIO],
        format: str,
        *args,
        **kwargs
    ) -> Union[JsonItemExporter, JsonLinesItemExporter, MarshalItemExporter, PickleItemExporter, CsvItemExporter, XmlItemExporter]: ...
    def _get_instance(
        self,
        objcls: Union[Type[JsonItemExporter], Type[MarshalItemExporter], Type[JsonLinesItemExporter], Type[PickleItemExporter], Type[CsvItemExporter], Type[FromCrawlerCsvItemExporter], Type[XmlItemExporter]],
        *args,
        **kwargs
    ) -> Union[JsonItemExporter, JsonLinesItemExporter, MarshalItemExporter, PickleItemExporter, CsvItemExporter, XmlItemExporter]: ...
    def _get_storage(
        self,
        uri: str,
        feed_options: Union[Dict[str, Optional[Union[str, List[str], int, Dict[Any, Any]]]], Dict[str, Optional[Union[str, Dict[str, bool], int]]], Dict[str, Optional[Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]], int, Dict[Any, Any]]]], Dict[str, Optional[Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]], bytes, int, Dict[Any, Any]]]], Dict[str, Optional[Union[str, List[str], List[Dict[str, int]], int, Dict[Any, Any]]]], Dict[str, Optional[Union[str, List[Union[Type[FeedPostProcessedExportsTest.MyPlugin1], str]], bytes, int, Dict[Any, Any]]]], Dict[str, Optional[Union[str, int, Dict[Any, Any]]]]]
    ) -> Union[FTPFeedStorageWithoutFeedOptions, DummyBlockingFeedStorage, StdoutFeedStorage, LogOnStoreFileStorage, FileFeedStorage, FTPFeedStorageWithoutFeedOptionsWithFromCrawler, S3FeedStorage]: ...
    def _handle_store_error(
        self,
        f: Failure,
        logmsg: str,
        spider: ItemSpider,
        slot_type: str
    ) -> None: ...
    def _handle_store_success(
        self,
        f: Optional[MagicMock],
        logmsg: str,
        spider: ItemSpider,
        slot_type: str
    ) -> None: ...
    def _load_components(
        self,
        setting_prefix: str
    ) -> Union[Dict[str, Union[Type[FileFeedStorage], Type[StdoutFeedStorageWithoutFeedOptions], Type[FTPFeedStorage], Type[GCSFeedStorage], Type[S3FeedStorage], Type[StdoutFeedStorage]]], Dict[str, Union[Type[FileFeedStorage], Type[LogOnStoreFileStorage], Type[FTPFeedStorage], Type[GCSFeedStorage], Type[S3FeedStorage], Type[StdoutFeedStorage]]], Dict[str, Union[Type[FileFeedStorage], Type[FailingBlockingFeedStorage], Type[FTPFeedStorage], Type[GCSFeedStorage], Type[S3FeedStorage], Type[StdoutFeedStorage]]], Dict[str, Union[Type[FileFeedStorage], Type[FileFeedStorageWithoutFeedOptions], Type[FTPFeedStorage], Type[GCSFeedStorage], Type[S3FeedStorage], Type[StdoutFeedStorage]]], Dict[str, Union[Type[FileFeedStorage], Type[FTPFeedStorageWithoutFeedOptions], Type[FTPFeedStorage], Type[GCSFeedStorage], Type[S3FeedStorage], Type[StdoutFeedStorage]]], Dict[str, Union[Type[FileFeedStorage], Type[S3FeedStorageWithoutFeedOptionsWithFromCrawler], Type[FTPFeedStorage], Type[GCSFeedStorage], Type[S3FeedStorage], Type[StdoutFeedStorage]]], Dict[str, Union[Type[FileFeedStorage], Type[DummyBlockingFeedStorage], Type[FTPFeedStorage], Type[GCSFeedStorage], Type[S3FeedStorage], Type[StdoutFeedStorage]]], Dict[str, Union[Type[FileFeedStorage], Type[FTPFeedStorage], Type[GCSFeedStorage], Type[S3FeedStorage], Type[StdoutFeedStorage]]], Dict[str, Union[Type[FileFeedStorage], Type[FromCrawlerFileFeedStorage], Type[FTPFeedStorage], Type[GCSFeedStorage], Type[S3FeedStorage], Type[StdoutFeedStorage]]], Dict[str, Union[Type[FileFeedStorage], Type[S3FeedStorageWithoutFeedOptions], Type[FTPFeedStorage], Type[GCSFeedStorage], Type[S3FeedStorage], Type[StdoutFeedStorage]]], Dict[str, Union[Type[JsonItemExporter], Type[JsonLinesItemExporter], Type[CsvItemExporter], Type[XmlItemExporter], Type[MarshalItemExporter], Type[PickleItemExporter]]], Dict[str, Union[Type[JsonItemExporter], Type[JsonLinesItemExporter], Type[FromCrawlerCsvItemExporter], Type[XmlItemExporter], Type[MarshalItemExporter], Type[PickleItemExporter]]], Dict[str, Union[Type[FileFeedStorage], Type[FTPFeedStorageWithoutFeedOptionsWithFromCrawler], Type[FTPFeedStorage], Type[GCSFeedStorage], Type[S3FeedStorage], Type[StdoutFeedStorage]]]]: ...
    def _load_filter(
        self,
        feed_options: Union[Dict[str, Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]], bytes]], Dict[str, Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]]]], Dict[str, Union[str, List[str], List[Dict[str, int]]]], Dict[str, Union[str, int]], Dict[str, Union[str, List[Union[Type[FeedPostProcessedExportsTest.MyPlugin1], str]], bytes]], Dict[str, str], Dict[str, Union[str, List[str]]], Dict[str, Optional[Union[str, List[str]]]], Dict[str, Optional[str]], Dict[str, Union[str, Dict[str, bool]]], Dict[str, Union[str, List[str], int]], Dict[str, Optional[Union[str, int]]], Dict[Any, Any]]
    ) -> ItemFilter: ...
    def _settings_are_valid(self) -> bool: ...
    def _start_new_batch(
        self,
        batch_id: int,
        uri: str,
        feed_options: Dict[str, Optional[Union[str, int, Dict[Any, Any]]]],
        spider: Spider,
        uri_template: str
    ) -> _FeedSlot: ...
    def _storage_supported(
        self,
        uri: str,
        feed_options: Union[Dict[str, Optional[Union[str, List[str], int, Dict[Any, Any]]]], Dict[str, Optional[Union[str, Dict[str, bool], int]]], Dict[str, Optional[Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]], int, Dict[Any, Any]]]], Dict[str, Optional[Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]], bytes, int, Dict[Any, Any]]]], Dict[str, Optional[Union[str, List[str], List[Dict[str, int]], int, Dict[Any, Any]]]], Dict[str, Optional[Union[str, int, Dict[Any, Any]]]], Dict[str, Optional[Union[str, List[Union[Type[FeedPostProcessedExportsTest.MyPlugin1], str]], bytes, int, Dict[Any, Any]]]], Dict[str, Optional[Union[int, Dict[Any, Any]]]]]
    ) -> Optional[bool]: ...
    def close_spider(self, spider: ItemSpider) -> DeferredList: ...
    @classmethod
    def from_crawler(cls, crawler: Crawler) -> FeedExporter: ...
    def item_scraped(self, item: Union[Dict[Any, Any], Item], spider: ItemSpider) -> None: ...
    def open_spider(self, spider: Spider) -> None: ...


class FileFeedStorage:
    def __init__(self, uri: str, *, feed_options = ...) -> None: ...
    def open(self, spider: Spider) -> BufferedWriter: ...
    def store(self, file: Union[PostProcessingManager, BufferedWriter]) -> None: ...


class GCSFeedStorage:
    def __init__(self, uri: str, project_id: str, acl: Optional[str]) -> None: ...
    @classmethod
    def from_crawler(cls, crawler: Crawler, uri: str) -> GCSFeedStorage: ...


class ItemFilter:
    def __init__(self, feed_options: Optional[dict]) -> None: ...
    def accepts(self, item: Any) -> bool: ...


class S3FeedStorage:
    def __init__(
        self,
        uri: str,
        access_key: Optional[str] = ...,
        secret_key: Optional[str] = ...,
        acl: Optional[str] = ...,
        endpoint_url: Optional[str] = ...,
        *,
        feed_options = ...,
        session_token = ...
    ) -> None: ...
    @classmethod
    def from_crawler(
        cls,
        crawler: Crawler,
        uri: str,
        *,
        feed_options = ...
    ) -> S3FeedStorage: ...


class StdoutFeedStorage:
    def __init__(self, uri: str, _stdout: Optional[BytesIO] = ..., *, feed_options = ...) -> None: ...
    def open(self, spider: Spider) -> Union[BytesIO, FileIO]: ...
    def store(self, file: Union[BytesIO, FileIO]) -> None: ...


class _FeedSlot:
    def __init__(
        self,
        file: Union[PostProcessingManager, BufferedWriter, _TemporaryFileWrapper, FileIO],
        exporter: Union[JsonItemExporter, JsonLinesItemExporter, MarshalItemExporter, PickleItemExporter, CsvItemExporter, XmlItemExporter],
        storage: Union[FTPFeedStorageWithoutFeedOptions, DummyBlockingFeedStorage, LogOnStoreFileStorage, StdoutFeedStorage, FileFeedStorage, FTPFeedStorageWithoutFeedOptionsWithFromCrawler, S3FeedStorage],
        uri: str,
        format: str,
        store_empty: bool,
        batch_id: int,
        uri_template: str,
        filter: ItemFilter
    ) -> None: ...
    def finish_exporting(self) -> None: ...
    def start_exporting(self) -> None: ...
