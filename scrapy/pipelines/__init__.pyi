from scrapy.item import Item
from scrapy.pipelines.files import FilesPipeline
from scrapy.settings import Settings
from tests.pipelines import (
    ProcessWithZeroDivisionErrorPipiline,
    ZeroDivisionErrorPipeline,
)
from tests.spiders import (
    AsyncDefAsyncioGenComplexSpider,
    AsyncDefAsyncioGenLoopSpider,
    AsyncDefAsyncioGenSpider,
    AsyncDefAsyncioReturnSingleElementSpider,
    AsyncDefAsyncioReturnSpider,
    ItemSpider,
)
from tests.test_engine import (
    AttrsItem,
    TestSpider,
)
from tests.test_logformatter import DropSomeItemsPipeline
from tests.test_pipeline_crawl import MediaDownloadSpider
from tests.test_pipelines import (
    AsyncDefAsyncioPipeline,
    AsyncDefNotAsyncioPipeline,
    AsyncDefPipeline,
    DeferredPipeline,
    ItemSpider,
    SimplePipeline,
)
from tests.test_scheduler_base import TestSpider
from tests.test_signals import ItemSpider
from tests.test_spidermiddleware_output_chain import (
    GeneratorCallbackSpider,
    GeneratorOutputChainSpider,
    NotGeneratorOutputChainSpider,
    ProcessSpiderInputSpiderWithErrback,
    RecoverySpider,
)
from twisted.internet.defer import Deferred
from typing import (
    Any,
    Dict,
    List,
    Type,
    Union,
)


class ItemPipelineManager:
    def _add_middleware(
        self,
        pipe: Union[AsyncDefAsyncioPipeline, AsyncDefPipeline, ZeroDivisionErrorPipeline, DeferredPipeline, DropSomeItemsPipeline, SimplePipeline, ProcessWithZeroDivisionErrorPipiline, FilesPipeline, AsyncDefNotAsyncioPipeline]
    ) -> None: ...
    @classmethod
    def _get_mwlist_from_settings(
        cls,
        settings: Settings
    ) -> List[Union[Type[DropSomeItemsPipeline], Type[AsyncDefPipeline], Type[DeferredPipeline], Type[SimplePipeline], Any, str, Type[AsyncDefAsyncioPipeline], Type[AsyncDefNotAsyncioPipeline]]]: ...
    def process_item(
        self,
        item: Union[AttrsItem, Dict[str, str], Dict[str, List[str]], Dict[Any, Any], Item, Dict[str, List[Union[Any, str]]], Dict[str, int]],
        spider: Union[ItemSpider, ItemSpider, RecoverySpider, NotGeneratorOutputChainSpider, AsyncDefAsyncioGenLoopSpider, TestSpider, AsyncDefAsyncioReturnSpider, GeneratorOutputChainSpider, ProcessSpiderInputSpiderWithErrback, AsyncDefAsyncioGenComplexSpider, ItemSpider, MediaDownloadSpider, AsyncDefAsyncioGenSpider, AsyncDefAsyncioReturnSingleElementSpider, TestSpider, GeneratorCallbackSpider]
    ) -> Deferred: ...
