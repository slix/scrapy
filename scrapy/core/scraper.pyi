from scrapy.crawler import Crawler
from scrapy.http.request import Request
from scrapy.http.response import Response
from scrapy.spiders import Spider
from twisted.internet.defer import (
    Deferred,
    DeferredList,
)
from twisted.python.failure import Failure
from typing import (
    Any,
    Iterable,
    Iterator,
    Optional,
    Tuple,
    Union,
)


class Scraper:
    def __init__(self, crawler: Crawler) -> None: ...
    def _check_if_closing(self, spider: Spider) -> None: ...
    def _itemproc_finished(
        self,
        output: Any,
        item: Any,
        response: Response,
        spider: Spider
    ) -> None: ...
    def _log_download_errors(
        self,
        spider_failure: Failure,
        download_failure: Failure,
        request: Request,
        spider: Spider
    ) -> Optional[Failure]: ...
    def _process_spidermw_output(
        self,
        output: Any,
        request: Request,
        response: Response,
        spider: Spider
    ) -> Optional[Deferred]: ...
    def _scrape(
        self,
        result: Union[Response, Failure],
        request: Request,
        spider: Spider
    ) -> Deferred: ...
    def _scrape2(
        self,
        result: Union[Response, Failure],
        request: Request,
        spider: Spider
    ) -> Deferred: ...
    def _scrape_next(self, spider: Spider) -> None: ...
    def call_spider(
        self,
        result: Union[Response, Failure],
        request: Request,
        spider: Spider
    ) -> Deferred: ...
    def close_spider(self, spider: Spider) -> Deferred: ...
    def enqueue_scrape(
        self,
        result: Union[Response, Failure],
        request: Request,
        spider: Spider
    ) -> Deferred: ...
    def handle_spider_error(
        self,
        _failure: Failure,
        request: Request,
        response: Response,
        spider: Spider
    ) -> None: ...
    def handle_spider_output(
        self,
        result: Iterable,
        request: Request,
        response: Response,
        spider: Spider
    ) -> Deferred: ...
    def is_idle(self) -> bool: ...
    def open_spider(self, spider: Spider) -> Iterator[DeferredList]: ...


class Slot:
    def __init__(self, max_active_size: int = ...) -> None: ...
    def add_response_request(
        self,
        result: Union[Response, Failure],
        request: Request
    ) -> Deferred: ...
    def finish_response(
        self,
        result: Union[Response, Failure],
        request: Request
    ) -> None: ...
    def is_idle(self) -> bool: ...
    def needs_backout(self) -> bool: ...
    def next_response_request_deferred(
        self
    ) -> Tuple[Union[Response, Failure], Request, Deferred]: ...
