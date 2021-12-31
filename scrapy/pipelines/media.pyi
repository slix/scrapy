from scrapy.crawler import Crawler
from scrapy.http.request import Request
from scrapy.http.response import Response
from scrapy.pipelines.files import FilesPipeline
from scrapy.settings import Settings
from scrapy.spiders import Spider
from tests.test_pipeline_files import ItemWithFiles
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
    Tuple,
    Union,
)


class MediaPipeline:
    def __init__(
        self,
        download_func: Optional[Callable] = ...,
        settings: Optional[Settings] = ...
    ) -> None: ...
    def _cache_result_and_execute_waiters(
        self,
        result: Optional[Union[Dict[str, str], Response, Failure, str, Dict[str, Optional[str]]]],
        fp: str,
        info: MediaPipeline.SpiderInfo
    ) -> None: ...
    def _check_media_to_download(
        self,
        result: Optional[Union[Dict[str, str], str]],
        request: Request,
        info: MediaPipeline.SpiderInfo,
        item: Union[Dict[str, List[Request]], ItemWithFiles, Dict[str, Request], Dict[str, List[Union[Any, str]]]]
    ) -> Union[Dict[str, str], str, Deferred]: ...
    def _check_signature(self, func: Callable) -> None: ...
    def _compatible(self, func: Callable) -> Callable: ...
    def _handle_statuses(self, allow_redirects: bool) -> None: ...
    def _key_for_pipe(
        self,
        key: str,
        base_class_name: Optional[str] = ...,
        settings: Optional[Settings] = ...
    ) -> str: ...
    def _make_compatible(self) -> None: ...
    def _modify_media_request(self, request: Request) -> None: ...
    def _process_request(
        self,
        request: Request,
        info: MediaPipeline.SpiderInfo,
        item: Union[Dict[str, List[Request]], Dict[str, List[Union[Any, str]]], Dict[str, Request], ItemWithFiles]
    ) -> Deferred: ...
    @classmethod
    def from_crawler(cls, crawler: Crawler) -> FilesPipeline: ...
    def get_media_requests(self, item: Dict[str, str], info: MediaPipeline.SpiderInfo) -> None: ...
    def item_completed(
        self,
        results: List[Union[Tuple[bool, str], Any, Tuple[bool, int], Tuple[bool, Failure], Tuple[bool, None], Tuple[bool, Response]]],
        item: Union[Dict[str, str], Dict[str, List[Request]], Dict[str, Request], Dict[str, Union[str, List[Union[Tuple[bool, int], Tuple[bool, Failure]]]]], Dict[str, Union[str, List[Any]]]],
        info: MediaPipeline.SpiderInfo
    ) -> Union[Dict[str, str], Dict[str, List[Request]], Dict[str, Request], Dict[str, Union[str, List[Union[Tuple[bool, int], Tuple[bool, Failure]]]]], Dict[str, Union[str, List[Any]]]]: ...
    def media_downloaded(
        self,
        response: Optional[Response],
        request: Request,
        info: MediaPipeline.SpiderInfo,
        *,
        item = ...
    ) -> Optional[Response]: ...
    def media_failed(
        self,
        failure: Failure,
        request: Request,
        info: MediaPipeline.SpiderInfo
    ) -> Failure: ...
    def media_to_download(
        self,
        request: Request,
        info: MediaPipeline.SpiderInfo,
        *,
        item = ...
    ) -> None: ...
    def open_spider(self, spider: Optional[Spider]) -> None: ...
    def process_item(
        self,
        item: Union[Dict[str, str], Dict[str, List[Request]], Dict[str, List[Union[Any, str]]], Dict[str, Request], ItemWithFiles],
        spider: Optional[Spider]
    ) -> DeferredList: ...


class MediaPipeline.SpiderInfo:
    def __init__(self, spider: Optional[Spider]) -> None: ...
