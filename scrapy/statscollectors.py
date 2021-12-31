"""
Scrapy extension for collecting scraping stats
"""
import pprint
import logging
from datetime import datetime
from scrapy.crawler import Crawler
from scrapy.spiders import Spider
from typing import Any, Dict, Optional, Union

logger = logging.getLogger(__name__)


class StatsCollector:

    def __init__(self, crawler: Crawler) -> None:
        self._dump = crawler.settings.getbool('STATS_DUMP')
        self._stats = {}

    def get_value(self, key: str, default: Optional[Union[int, str]]=None, spider: Optional[Spider]=None) -> Optional[Union[int, str, float]]:
        return self._stats.get(key, default)

    def get_stats(self, spider: Optional[Union[Spider, str]]=None) -> Union[Dict[str, str], Dict[Any, Any], Dict[str, Union[str, int]], Dict[str, int], Dict[str, Union[datetime, int, float, str]]]:
        return self._stats

    def set_value(self, key: str, value: Union[str, datetime, int, float], spider: Optional[Spider]=None) -> None:
        self._stats[key] = value

    def set_stats(self, stats, spider=None):
        self._stats = stats

    def inc_value(self, key: str, count: int=1, start: int=0, spider: Optional[Spider]=None) -> None:
        d = self._stats
        d[key] = d.setdefault(key, start) + count

    def max_value(self, key: str, value: int, spider: Optional[Spider]=None) -> None:
        self._stats[key] = max(self._stats.setdefault(key, value), value)

    def min_value(self, key: str, value: int, spider: None=None) -> None:
        self._stats[key] = min(self._stats.setdefault(key, value), value)

    def clear_stats(self, spider=None):
        self._stats.clear()

    def open_spider(self, spider: Union[Spider, str]) -> None:
        pass

    def close_spider(self, spider: Spider, reason: str) -> None:
        if self._dump:
            logger.info("Dumping Scrapy stats:\n" + pprint.pformat(self._stats),
                        extra={'spider': spider})
        self._persist_stats(self._stats, spider)

    def _persist_stats(self, stats: Dict[str, int], spider: Spider) -> None:
        pass


class MemoryStatsCollector(StatsCollector):

    def __init__(self, crawler: Crawler) -> None:
        super().__init__(crawler)
        self.spider_stats = {}

    def _persist_stats(self, stats: Union[Dict[str, int], Dict[str, Union[datetime, int, float, str]]], spider: Spider) -> None:
        self.spider_stats[spider.name] = stats


class DummyStatsCollector(StatsCollector):

    def get_value(self, key: str, default: Optional[str]=None, spider: None=None) -> Optional[str]:
        return default

    def set_value(self, key: str, value: Union[datetime, str, float], spider: Optional[Spider]=None) -> None:
        pass

    def set_stats(self, stats, spider=None):
        pass

    def inc_value(self, key: str, count: int=1, start: int=0, spider: Optional[Spider]=None) -> None:
        pass

    def max_value(self, key: str, value: int, spider: None=None) -> None:
        pass

    def min_value(self, key: str, value: int, spider: None=None) -> None:
        pass
