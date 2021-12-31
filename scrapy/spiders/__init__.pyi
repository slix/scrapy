from logging import LoggerAdapter
from scrapy.crawler import Crawler
from scrapy.http.request import Request
from scrapy.http.response import Response
from scrapy.http.response.text import TextResponse
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
from tests.test_crawler import NoRequestsSpider
from tests.test_engine import TestSpider
from tests.test_pipelines import ItemSpider
from tests.test_request_cb_kwargs import KeywordArgumentsSpider
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
from typing import (
    Any,
    Dict,
    Iterator,
    List,
    Optional,
    Union,
)


class Spider:
    def __init__(self, name: Optional[str] = ..., **kwargs) -> None: ...
    def __str__(self) -> str: ...
    def _parse(
        self,
        response: Response,
        **kwargs
    ) -> Optional[Union[List[Dict[str, List[str]]], Dict[str, str], Iterator[Any], Request, Dict[str, int]]]: ...
    def _set_crawler(self, crawler: Crawler) -> None: ...
    @staticmethod
    def close(
        spider: Union[HeadersReceivedCallbackSpider, DuplicateStartRequestsSpider, ItemSpider, DelaySpider, GeneratorCallbackSpider, ProcessSpiderInputSpiderWithoutErrback, NoRequestsSpider, ItemSpider, RecoverySpider, StartUrlsSpider, BytesReceivedCallbackSpider, KeywordArgumentsSpider, CrawlSpiderWithParseMethod, TestSpider, SingleRequestSpider, SimpleSpider, FollowAllSpider, NotGeneratorOutputChainSpider, NotGeneratorCallbackSpider, _HttpErrorSpider, TestSpider, GeneratorOutputChainSpider],
        reason: str
    ) -> None: ...
    @classmethod
    def from_crawler(cls, crawler: Crawler, *args, **kwargs) -> Spider: ...
    def log(self, message: str, level: str = ..., **kw) -> None: ...
    @property
    def logger(self) -> LoggerAdapter: ...
    def parse(self, response: TextResponse, **kwargs): ...
    def start_requests(self) -> Iterator[Request]: ...
    @classmethod
    def update_settings(cls, settings: Settings) -> None: ...
