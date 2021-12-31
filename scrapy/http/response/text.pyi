from parsel.selector import Selector
from scrapy.http.request import Request
from scrapy.link import Link
from scrapy.selector.unified import (
    Selector,
    SelectorList,
)
from typing import (
    Any,
    Dict,
    Generator,
    List,
    Optional,
    Union,
)
from unittest.mock import MagicMock


def _url_from_selector(sel: Selector) -> str: ...


class TextResponse:
    def __init__(self, *args, **kwargs) -> None: ...
    def _auto_detect_fun(self, text: bytes) -> Optional[str]: ...
    def _body_declared_encoding(self) -> Optional[str]: ...
    def _body_inferred_encoding(self) -> str: ...
    def _declared_encoding(self) -> Optional[str]: ...
    def _headers_encoding(self) -> Optional[str]: ...
    def _set_body(self, body: Union[bytes, str]) -> None: ...
    def _set_url(self, url: Union[bytes, str]) -> None: ...
    def body_as_unicode(self) -> str: ...
    def css(self, query: str) -> SelectorList: ...
    @property
    def encoding(self) -> str: ...
    def follow(
        self,
        url: Optional[Union[Link, Selector, str, SelectorList]],
        callback: None = ...,
        method: str = ...,
        headers: None = ...,
        body: None = ...,
        cookies: None = ...,
        meta: None = ...,
        encoding: None = ...,
        priority: int = ...,
        dont_filter: bool = ...,
        errback: None = ...,
        cb_kwargs: None = ...,
        flags: Optional[List[str]] = ...
    ) -> Request: ...
    def follow_all(
        self,
        urls: Optional[Union[List[None], List[str], List[Any], int, SelectorList]] = ...,
        callback: None = ...,
        method: str = ...,
        headers: None = ...,
        body: None = ...,
        cookies: None = ...,
        meta: None = ...,
        encoding: None = ...,
        priority: int = ...,
        dont_filter: bool = ...,
        errback: None = ...,
        cb_kwargs: None = ...,
        flags: Optional[List[str]] = ...,
        css: Optional[str] = ...,
        xpath: Optional[str] = ...
    ) -> Generator[Request, None, None]: ...
    def json(self) -> Union[MagicMock, Dict[str, str]]: ...
    @property
    def selector(self) -> Selector: ...
    @property
    def text(self) -> str: ...
    def urljoin(self, url: str) -> str: ...
    def xpath(self, query: str, **kwargs) -> SelectorList: ...
