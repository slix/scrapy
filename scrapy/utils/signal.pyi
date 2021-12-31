from pydispatch.dispatcher import (
    _Anonymous,
    _Any,
)
from scrapy.crawler import Crawler
from twisted.internet.defer import (
    Deferred,
    DeferredList,
)
from twisted.python.failure import Failure
from typing import (
    Any,
    Callable,
    List,
    Tuple,
    Union,
)


def disconnect_all(signal: object = ..., sender: _Any = ...) -> None: ...


def send_catch_log(
    signal: object = ...,
    sender: Union[_Anonymous, Crawler] = ...,
    *arguments,
    **named
) -> List[Union[Tuple[Callable, Failure], Any, Tuple[Callable, Deferred], Tuple[Callable, str], Tuple[Callable, None]]]: ...


def send_catch_log_deferred(
    signal: object = ...,
    sender: Union[_Anonymous, Crawler] = ...,
    *arguments,
    **named
) -> DeferredList: ...
