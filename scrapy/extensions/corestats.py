"""
Extension for collecting core stats like items scraped and start/finish times
"""
from datetime import datetime

from scrapy import signals
from scrapy.crawler import Crawler
from scrapy.exceptions import DropItem
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.statscollectors import StatsCollector
from tests.test_engine import AttrsItem
from typing import Any, Dict, List, Optional, Union


class CoreStats:

    def __init__(self, stats: StatsCollector) -> None:
        self.stats = stats
        self.start_time = None

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> CoreStats:
        o = cls(crawler.stats)
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(o.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(o.item_scraped, signal=signals.item_scraped)
        crawler.signals.connect(o.item_dropped, signal=signals.item_dropped)
        crawler.signals.connect(o.response_received, signal=signals.response_received)
        return o

    def spider_opened(self, spider: Spider) -> None:
        self.start_time = datetime.utcnow()
        self.stats.set_value('start_time', self.start_time, spider=spider)

    def spider_closed(self, spider: Spider, reason: str) -> None:
        finish_time = datetime.utcnow()
        elapsed_time = finish_time - self.start_time
        elapsed_time_seconds = elapsed_time.total_seconds()
        self.stats.set_value('elapsed_time_seconds', elapsed_time_seconds, spider=spider)
        self.stats.set_value('finish_time', finish_time, spider=spider)
        self.stats.set_value('finish_reason', reason, spider=spider)

    def item_scraped(self, item: Optional[Union[Item, Dict[str, List[Union[Dict[str, str], str]]], AttrsItem, Dict[Any, Any], Dict[str, List[str]], Dict[str, List[Union[Any, str]]], Dict[str, int], Dict[str, str]]], spider: Spider) -> None:
        self.stats.inc_value('item_scraped_count', spider=spider)

    def response_received(self, spider: Spider) -> None:
        self.stats.inc_value('response_received_count', spider=spider)

    def item_dropped(self, item: Union[Dict[Any, Any], Item], spider: Spider, exception: Union[ZeroDivisionError, DropItem]) -> None:
        reason = exception.__class__.__name__
        self.stats.inc_value('item_dropped_count', spider=spider)
        self.stats.inc_value(f'item_dropped_reasons_count/{reason}', spider=spider)
