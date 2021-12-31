from tests.test_request_dict import (
    TestSpider,
    TestSpiderDelegation,
)
from typing import (
    Callable,
    List,
    Optional,
    Type,
    Union,
)


def _find_method(
    obj: Optional[Union[TestSpiderDelegation, TestSpider]],
    func: Callable
) -> str: ...


class Request:
    def __init__(
        self,
        url: str,
        callback: Optional[Callable] = ...,
        method: str = ...,
        headers: Optional[dict] = ...,
        body: Optional[Union[bytes, str]] = ...,
        cookies: Optional[Union[dict, List[dict]]] = ...,
        meta: Optional[dict] = ...,
        encoding: str = ...,
        priority: int = ...,
        dont_filter: bool = ...,
        errback: Optional[Callable] = ...,
        flags: Optional[List[str]] = ...,
        cb_kwargs: Optional[dict] = ...
    ) -> None: ...
    def __str__(self) -> str: ...
    def _get_body(self) -> bytes: ...
    def _get_url(self) -> str: ...
    def _set_body(self, body: Optional[Union[bytes, str]]) -> None: ...
    def _set_url(self, url: str) -> None: ...
    @property
    def cb_kwargs(self) -> dict: ...
    def copy(self) -> Request: ...
    @property
    def encoding(self) -> str: ...
    @classmethod
    def from_curl(
        cls: Type[~RequestTypeVar],
        curl_command: str,
        ignore_unknown_options: bool = ...,
        **kwargs
    ) -> RequestTypeVar: ...
    @property
    def meta(self) -> dict: ...
    def replace(self, *args, **kwargs) -> Request: ...
    def to_dict(self, *, spider: Optional['scrapy.Spider'] = ...) -> dict: ...
