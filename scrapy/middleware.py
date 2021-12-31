import logging
import pprint
from collections import defaultdict, deque
from typing import Any, Iterator, List, Optional, Union, Callable, Deque, Dict

from twisted.internet.defer import Deferred

from scrapy import Spider
from scrapy.exceptions import NotConfigured
from scrapy.settings import Settings
from scrapy.utils.misc import create_instance, load_object
from scrapy.utils.defer import process_parallel, process_chain, process_chain_both
from scrapy.core.downloader.middleware import DownloaderMiddlewareManager
from scrapy.core.spidermw import SpiderMiddlewareManager
from scrapy.crawler import Crawler
from scrapy.extension import ExtensionManager
from scrapy.extensions.closespider import CloseSpider
from scrapy.extensions.corestats import CoreStats
from scrapy.extensions.feedexport import FeedExporter
from scrapy.extensions.logstats import LogStats
from scrapy.extensions.memusage import MemoryUsage
from scrapy.extensions.spiderstate import SpiderState
from scrapy.extensions.telnet import TelnetConsole
from scrapy.extensions.throttle import AutoThrottle
from scrapy.item import Item
from scrapy.pipelines import ItemPipelineManager
from scrapy.pipelines.files import FilesPipeline
from scrapy.spidermiddlewares.depth import DepthMiddleware
from scrapy.spidermiddlewares.httperror import HttpErrorMiddleware
from scrapy.spidermiddlewares.offsite import OffsiteMiddleware
from scrapy.spidermiddlewares.referer import RefererMiddleware
from scrapy.spidermiddlewares.urllength import UrlLengthMiddleware
from scrapy.spiders import Spider
from tests.pipelines import ProcessWithZeroDivisionErrorPipiline, ZeroDivisionErrorPipeline
from tests.test_engine import AttrsItem
from tests.test_logformatter import DropSomeItemsPipeline
from tests.test_middleware import M1, M2, M3, TestMiddlewareManager
from tests.test_pipelines import AsyncDefAsyncioPipeline, AsyncDefNotAsyncioPipeline, AsyncDefPipeline, DeferredPipeline, SimplePipeline
from tests.test_request_cb_kwargs import InjectArgumentsSpiderMiddleware
from tests.test_spidermiddleware_output_chain import FailProcessSpiderInputMiddleware, GeneratorDoNothingAfterFailureMiddleware, GeneratorDoNothingAfterRecoveryMiddleware, GeneratorFailMiddleware, GeneratorRecoverMiddleware, LogExceptionMiddleware, NotGeneratorDoNothingAfterFailureMiddleware, NotGeneratorDoNothingAfterRecoveryMiddleware, NotGeneratorFailMiddleware, NotGeneratorRecoverMiddleware, RecoveryMiddleware

logger = logging.getLogger(__name__)


class MiddlewareManager:
    """Base class for implementing middleware managers"""

    component_name = 'foo middleware'

    def __init__(self, *middlewares) -> None:
        self.middlewares = middlewares
        self.methods: Dict[str, Deque[Callable]] = defaultdict(deque)
        for mw in middlewares:
            self._add_middleware(mw)

    @classmethod
    def _get_mwlist_from_settings(cls, settings: Settings) -> list:
        raise NotImplementedError

    @classmethod
    def from_settings(cls, settings: Settings, crawler: Optional[Crawler]=None) -> Union[DownloaderMiddlewareManager, ExtensionManager, TestMiddlewareManager, ItemPipelineManager, SpiderMiddlewareManager]:
        mwlist = cls._get_mwlist_from_settings(settings)
        middlewares = []
        enabled = []
        for clspath in mwlist:
            try:
                mwcls = load_object(clspath)
                mw = create_instance(mwcls, settings, crawler)
                middlewares.append(mw)
                enabled.append(clspath)
            except NotConfigured as e:
                if e.args:
                    clsname = clspath.split('.')[-1]
                    logger.warning("Disabled %(clsname)s: %(eargs)s",
                                   {'clsname': clsname, 'eargs': e.args[0]},
                                   extra={'crawler': crawler})

        logger.info("Enabled %(componentname)ss:\n%(enabledlist)s",
                    {'componentname': cls.component_name,
                     'enabledlist': pprint.pformat(enabled)},
                    extra={'crawler': crawler})
        return cls(*middlewares)

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> Union[ItemPipelineManager, ExtensionManager, DownloaderMiddlewareManager, SpiderMiddlewareManager]:
        return cls.from_settings(crawler.settings, crawler)

    def _add_middleware(self, mw: Union[RecoveryMiddleware, AsyncDefPipeline, UrlLengthMiddleware, GeneratorRecoverMiddleware, GeneratorFailMiddleware, M3, NotGeneratorDoNothingAfterRecoveryMiddleware, M1, SpiderState, NotGeneratorDoNothingAfterFailureMiddleware, InjectArgumentsSpiderMiddleware, AsyncDefAsyncioPipeline, ZeroDivisionErrorPipeline, GeneratorDoNothingAfterRecoveryMiddleware, OffsiteMiddleware, SimplePipeline, DeferredPipeline, RefererMiddleware, MemoryUsage, TelnetConsole, GeneratorDoNothingAfterFailureMiddleware, CoreStats, LogExceptionMiddleware, AutoThrottle, FilesPipeline, DropSomeItemsPipeline, M2, DepthMiddleware, HttpErrorMiddleware, NotGeneratorRecoverMiddleware, FeedExporter, LogStats, FailProcessSpiderInputMiddleware, NotGeneratorFailMiddleware, AsyncDefNotAsyncioPipeline, ProcessWithZeroDivisionErrorPipiline, CloseSpider]) -> None:
        if hasattr(mw, 'open_spider'):
            self.methods['open_spider'].append(mw.open_spider)
        if hasattr(mw, 'close_spider'):
            self.methods['close_spider'].appendleft(mw.close_spider)

    def _process_parallel(self, methodname: str, obj: Spider, *args) -> Deferred:
        return process_parallel(self.methods[methodname], obj, *args)

    def _process_chain(self, methodname: str, obj: Union[Dict[str, List[Union[Any, str]]], Dict[str, List[str]], Dict[str, str], Dict[Any, Any], Iterator[Any], Dict[str, int], List[Any], AttrsItem, Item], *args
    ) -> Deferred:
        return process_chain(self.methods[methodname], obj, *args)

    def _process_chain_both(self, cb_methodname: str, eb_methodname: str, obj, *args) -> Deferred:
        return process_chain_both(self.methods[cb_methodname],
                                  self.methods[eb_methodname], obj, *args)

    def open_spider(self, spider: Spider) -> Deferred:
        return self._process_parallel('open_spider', spider)

    def close_spider(self, spider: Spider) -> Deferred:
        return self._process_parallel('close_spider', spider)
