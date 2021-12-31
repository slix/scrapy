from ipaddress import IPv4Address
from scrapy.core.downloader.contextfactory import ScrapyClientContextFactory
from scrapy.crawler import Crawler
from scrapy.http.headers import Headers
from scrapy.http.request import Request
from scrapy.http.response import Response
from scrapy.settings import Settings
from scrapy.spiders import Spider
from twisted.internet._sslverify import Certificate
from twisted.internet.asyncioreactor import AsyncioSelectorReactor
from twisted.internet.defer import (
    Deferred,
    DeferredList,
)
from twisted.internet.epollreactor import EPollReactor
from twisted.python.failure import Failure
from twisted.web._newclient import (
    HTTP11ClientProtocol,
    LengthEnforcingConsumer,
    Response,
)
from twisted.web.client import (
    Agent,
    HTTPConnectionPool,
    URI,
    _HTTP11ClientFactory,
)
from twisted.web.http_headers import Headers
from typing import (
    Dict,
    List,
    Optional,
    Tuple,
    Union,
)


def tunnel_request_data(
    host: Union[bytes, str],
    port: Union[int, str],
    proxy_auth_header: Optional[bytes] = ...
) -> bytes: ...


class HTTP11DownloadHandler:
    def __init__(self, settings: Settings, crawler: Optional[Crawler] = ...) -> None: ...
    def close(self) -> DeferredList: ...
    def download_request(
        self,
        request: Request,
        spider: Spider
    ) -> Deferred: ...
    @classmethod
    def from_crawler(
        cls,
        crawler: Crawler
    ) -> HTTP11DownloadHandler: ...


class ScrapyAgent:
    def __init__(
        self,
        contextFactory: Optional[ScrapyClientContextFactory] = ...,
        connectTimeout: int = ...,
        bindAddress: None = ...,
        pool: Optional[HTTPConnectionPool] = ...,
        maxsize: int = ...,
        warnsize: int = ...,
        fail_on_dataloss: bool = ...,
        crawler: Optional[Crawler] = ...
    ) -> None: ...
    def _cb_bodydone(
        self,
        result: Union[Dict[str, Optional[Union[Response, bytes, IPv4Address]]], Dict[str, Optional[Union[Response, bytes, List[str], IPv4Address]]], Dict[str, Optional[Union[Response, bytes, List[str]]]], Dict[str, Optional[Union[Response, bytes]]], Dict[str, Optional[Union[Response, bytes, List[str], IPv4Address, Failure]]], Dict[str, Optional[Union[Response, bytes, List[str], Failure]]], Dict[str, Optional[Union[Response, bytes, List[str], Certificate, IPv4Address]]], Dict[str, Optional[Union[Response, bytes, Certificate, IPv4Address]]]],
        request: Request,
        url: str
    ) -> Union[Failure, Response]: ...
    def _cb_bodyready(
        self,
        txresponse: Response,
        request: Request
    ) -> Union[Dict[str, Optional[Union[Response, bytes, List[str], Failure]]], Dict[str, Optional[Union[Response, bytes]]], Deferred, Dict[str, Optional[Union[Response, bytes, List[str]]]]]: ...
    def _cb_latency(
        self,
        result: Response,
        request: Request,
        start_time: float
    ) -> Response: ...
    def _cb_timeout(
        self,
        result: Union[Response, Failure],
        request: Request,
        url: str,
        timeout: Union[int, float]
    ) -> Union[Response, Failure]: ...
    def _get_agent(self, request: Request, timeout: Union[int, float]) -> Agent: ...
    @staticmethod
    def _headers_from_twisted_response(response: Response) -> Headers: ...
    def download_request(self, request: Request) -> Deferred: ...


class ScrapyProxyAgent:
    def __init__(
        self,
        reactor: Union[AsyncioSelectorReactor, EPollReactor],
        proxyURI: bytes,
        connectTimeout: Optional[int] = ...,
        bindAddress: None = ...,
        pool: Optional[HTTPConnectionPool] = ...
    ) -> None: ...
    def request(
        self,
        method: bytes,
        uri: bytes,
        headers: Optional[Headers] = ...,
        bodyProducer: None = ...
    ) -> Deferred: ...


class TunnelingAgent:
    def __init__(
        self,
        reactor: Union[AsyncioSelectorReactor, EPollReactor],
        proxyConf: Union[Tuple[str, int, bytes], Tuple[str, int, None]],
        contextFactory: Optional[ScrapyClientContextFactory] = ...,
        connectTimeout: Optional[float] = ...,
        bindAddress: None = ...,
        pool: Optional[HTTPConnectionPool] = ...
    ) -> None: ...
    def _getEndpoint(
        self,
        uri: URI
    ) -> TunnelingTCP4ClientEndpoint: ...
    def _requestWithEndpoint(
        self,
        key: Tuple[bytes, bytes, int],
        endpoint: TunnelingTCP4ClientEndpoint,
        method: bytes,
        parsedURI: URI,
        headers: Headers,
        bodyProducer: None,
        requestPath: bytes
    ) -> Deferred: ...


class TunnelingTCP4ClientEndpoint:
    def __init__(
        self,
        reactor: Union[AsyncioSelectorReactor, EPollReactor],
        host: bytes,
        port: int,
        proxyConf: Union[Tuple[str, int, bytes], Tuple[str, int, None]],
        contextFactory: ScrapyClientContextFactory,
        timeout: float = ...,
        bindAddress: None = ...
    ) -> None: ...
    def connect(self, protocolFactory: _HTTP11ClientFactory) -> Deferred: ...
    def processProxyResponse(self, rcvd_bytes: bytes) -> None: ...
    def requestTunnel(
        self,
        protocol: HTTP11ClientProtocol
    ) -> HTTP11ClientProtocol: ...


class _RequestBodyProducer:
    def __init__(self, body: bytes) -> None: ...
    def pauseProducing(self) -> None: ...
    def startProducing(
        self,
        consumer: LengthEnforcingConsumer
    ) -> Deferred: ...


class _ResponseReader:
    def __init__(
        self,
        finished: Deferred,
        txresponse: Response,
        request: Request,
        maxsize: int,
        warnsize: int,
        fail_on_dataloss: bool,
        crawler: Crawler
    ) -> None: ...
    def _finish_response(
        self,
        flags: Optional[List[str]] = ...,
        failure: Optional[Failure] = ...
    ) -> None: ...
    def connectionLost(self, reason: Failure) -> None: ...
    def connectionMade(self) -> None: ...
    def dataReceived(self, bodyBytes: bytes) -> None: ...
