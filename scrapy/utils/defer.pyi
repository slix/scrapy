from _asyncio import Future
from scrapy.http.request import Request
from scrapy.http.response import Response
from scrapy.item import Item
from scrapy.spiders import Spider
from tests.test_engine import AttrsItem
from twisted.internet.defer import (
    Deferred,
    DeferredList,
)
from twisted.python.failure import Failure
from typing import (
    Any,
    Callable,
    Coroutine,
    Dict,
    Generator,
    Iterable,
    Iterator,
    List,
    Optional,
    Union,
)
from unittest.mock import MagicMock


def defer_fail(_failure: Failure) -> Deferred: ...


def defer_result(
    result: Optional[Union[List[int], Failure, Response, Dict[str, str], Deferred, str, Dict[str, Optional[str]], MagicMock]]
) -> Deferred: ...


def defer_succeed(
    result: Optional[Union[List[int], Response, Dict[str, str], str, Dict[str, Optional[str]], MagicMock]]
) -> Deferred: ...


def deferred_f_from_coro_f(coro_f: Callable[..., Coroutine]) -> Callable: ...


def deferred_from_coro(
    o: Optional[Union[Dict[str, int], int, Response, Deferred, Request]]
) -> Any: ...


def deferred_to_future(d: Deferred) -> Future: ...


def iter_errback(iterable: Iterable, errback: Callable, *a, **kw) -> Generator: ...


def maybeDeferred_coro(f: Callable, *args, **kw) -> Deferred: ...


def maybe_deferred_to_future(
    d: Deferred
) -> Union[Deferred, Future]: ...


def mustbe_deferred(f: Callable, *args, **kw) -> Deferred: ...


def parallel(iterable: Iterable, count: int, callable: Callable, *args, **named) -> DeferredList: ...


def process_chain(
    callbacks: Iterable[Callable],
    input: Union[List[Any], Dict[str, int], Dict[Any, Any], Dict[str, List[Union[Any, str]]], AttrsItem, Item, str, Dict[str, List[str]], Dict[str, str], Iterator[Any]],
    *a,
    **kw
) -> Deferred: ...


def process_chain_both(
    callbacks: Iterable[Callable],
    errbacks: Iterable[Callable],
    input: Union[str, Failure],
    *a,
    **kw
) -> Deferred: ...


def process_parallel(
    callbacks: Iterable[Callable],
    input: Union[str, Spider],
    *a,
    **kw
) -> Deferred: ...
