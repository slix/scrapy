"""This module provides some functions and classes to record and report
references to live object instances.

If you want live objects for a particular class to be tracked, you only have to
subclass from object_ref (instead of object).

About performance: This library has a minimal performance impact when enabled,
and no performance penalty at all when disabled (as object_ref becomes just an
alias to object in that case).
"""

from collections import defaultdict
from operator import itemgetter
from time import time
from typing import Any, Iterator, Optional, Type, Union, DefaultDict
from weakref import WeakKeyDictionary
from scrapy.http.request import Request
from scrapy.http.response import Response
from scrapy.item import _BaseItem
from scrapy.selector.unified import Selector
from scrapy.spiders import Spider
from tests.test_utils_trackref import Bar, Foo


NoneType = type(None)
live_refs: DefaultDict[type, WeakKeyDictionary] = defaultdict(WeakKeyDictionary)


class object_ref:
    """Inherit from this class to a keep a record of live instances"""

    __slots__ = ()

    def __new__(cls: Union[Type[CSVFeedSpider], Type[FunctionProcessorItem], Type[TestItem], Type[InheritsTestSpider], Type[AsyncDefAsyncioGenComplexSpider], Type[FormRequest], Type[ItemZeroDivisionErrorSpider], Type[NotGeneratorOutputChainSpider], Type[TestSpider], Type[DictItem], Type[HeadersReceivedCallbackSpider], Type[AsyncDefAsyncioSpider], Type[Item], Type[GeneratorCallbackSpider], Type[Spider], Type[BrokenLinksMediaDownloadSpider], Type[Bar], Type[ItemSpider], Type[TextResponse], Type[TestSpider], Type[TestSpiderLegacy], Type[AsyncDefAsyncioReturnSpider], Type[MediaDownloadSpider], Type[BaseItem], Type[DataClassItemsSpider], Type[TestItem], Type[FilesPipelineTestItem], Type[CrawlSpiderWithErrback], Type[SingleRequestSpider], Type[TestItem], Type[CustomResponse], Type[XmlRpcRequest], Type[TestSpider], Type[DefaultSpider], Type[crawl.CrawlSpider], Type[TestSpiderAny], Type[TestNestedItem], Type[HeadersReceivedErrbackSpider], Type[KeywordArgumentsSpider], Type[CustomContractFailSpider], Type[TestItem], Type[AsyncDefAsyncioReqsReturnSpider], Type[ItemSpider], Type[Foo], Type[GeneratorCallbackSpiderMiddlewareRightAfterSpider], Type[TestItem], Type[DictItemsSpider], Type[FollowAllSpider], Type[AttrsItemsSpider], Type[DelaySpider], Type[RecoverySpider], Type[AsyncDefAsyncioReturnSingleElementSpider], Type[DummySpider], Type[NoInputReprocessingItem], Type[BytesReceivedErrbackSpider], Type[TestItem], Type[ProcessSpiderInputSpiderWithErrback], Type[ImagesPipelineTestItem], Type[GeneratorOutputChainSpider], Type[TestDupeFilterSpider], Type[RedirectedMediaDownloadSpider], Type[TestSpider], Type[NotGeneratorCallbackSpiderMiddlewareRightAfterSpider], Type[BrokenStartRequestsSpider], Type[ChangeCloseReasonSpider], Type[HtmlResponse], Type[ProcessSpiderInputSpiderWithoutErrback], Type[CustomContractSuccessSpider], Type[NameItem], Type[CustomFieldItem], Type[init.InitSpider], Type[AlternativeCallbacksSpider], Type[AsyncDefSpider], Type[XmlResponse], Type[StartUrlsSpider], Type[BytesReceivedCallbackSpider], Type[AsyncDefAsyncioGenSpider], Type[TestSpider], Type[_BaseItem], Type[AsyncDefAsyncioGenLoopSpider], Type[CrawlSpiderWithParseMethod], Type[Request], Type[CustomItem], Type[SimpleSpider], Type[SignalCatcherSpider], Type[_HttpErrorSpider], Type[NotGeneratorCallbackSpider], Type[ErrorSpider], Type[ItemWithFiles], Type[XMLFeedSpider], Type[Selector], Type[Response], Type[NoRequestsSpider], Type[ItemSpider], Type[CustomRequest], Type[json_request.JsonRequest], Type[sitemap.SitemapSpider], Type[DuplicateStartRequestsSpider]], *args,
        **kwargs
    ) -> Union[Bar, Spider, Response, _BaseItem, Request, Foo, Selector]:
        obj = object.__new__(cls)
        live_refs[cls][obj] = time()
        return obj


def format_live_refs(ignore: Union[Type[Foo], Type[None]]=NoneType) -> str:
    """Return a tabular representation of tracked objects"""
    s = "Live References\n\n"
    now = time()
    for cls, wdict in sorted(live_refs.items(),
                             key=lambda x: x[0].__name__):
        if not wdict:
            continue
        if issubclass(cls, ignore):
            continue
        oldest = min(wdict.values())
        s += f"{cls.__name__:<30} {len(wdict):6}   oldest: {int(now - oldest)}s ago\n"
    return s


def print_live_refs(*a, **kw) -> None:
    """Print tracked objects"""
    print(format_live_refs(*a, **kw))


def get_oldest(class_name: str) -> Optional[Union[Foo, Bar]]:
    """Get the oldest object for a specific class name"""
    for cls, wdict in live_refs.items():
        if cls.__name__ == class_name:
            if not wdict:
                break
            return min(wdict.items(), key=itemgetter(1))[0]


def iter_all(class_name: str) -> Iterator[Any]:
    """Iterate over all objects of the same class by its class name"""
    for cls, wdict in live_refs.items():
        if cls.__name__ == class_name:
            return wdict.keys()
