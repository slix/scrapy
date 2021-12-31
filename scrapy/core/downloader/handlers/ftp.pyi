from scrapy.crawler import Crawler
from scrapy.http.request import Request
from scrapy.http.response import Response
from scrapy.http.response.text import TextResponse
from scrapy.settings import Settings
from twisted.internet.defer import (
    Deferred,
    DeferredList,
)
from twisted.protocols.ftp import FTPClient
from twisted.python.failure import Failure
from typing import (
    List,
    Optional,
    Tuple,
    Union,
)


class FTPDownloadHandler:
    def __init__(self, settings: Settings) -> None: ...
    def _build_response(
        self,
        result: List[Union[Tuple[bool, List[Tuple[bool, List[str]]]], Tuple[bool, None]]],
        request: Request,
        protocol: ReceivedDataProtocol
    ) -> TextResponse: ...
    def _failed(
        self,
        result: Failure,
        request: Request
    ) -> Response: ...
    def download_request(self, request: Request, spider: None) -> Deferred: ...
    @classmethod
    def from_crawler(cls, crawler: Crawler) -> FTPDownloadHandler: ...
    def gotClient(
        self,
        client: FTPClient,
        request: Request,
        filepath: str
    ) -> DeferredList: ...


class ReceivedDataProtocol:
    def __init__(self, filename: Optional[bytes] = ...) -> None: ...
    def close(self) -> None: ...
    def dataReceived(self, data: bytes) -> None: ...
    @property
    def filename(self) -> Optional[bytes]: ...
