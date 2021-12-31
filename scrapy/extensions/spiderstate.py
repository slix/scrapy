import os
import pickle

from scrapy import signals
from scrapy.exceptions import NotConfigured
from scrapy.utils.job import job_dir
from scrapy.crawler import Crawler
from scrapy.spiders import Spider
from typing import Optional


class SpiderState:
    """Store and load spider state during a scraping job"""

    def __init__(self, jobdir: Optional[str]=None) -> None:
        self.jobdir = jobdir

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> SpiderState:
        jobdir = job_dir(crawler.settings)
        if not jobdir:
            raise NotConfigured

        obj = cls(jobdir)
        crawler.signals.connect(obj.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(obj.spider_opened, signal=signals.spider_opened)
        return obj

    def spider_closed(self, spider: Spider) -> None:
        if self.jobdir:
            with open(self.statefn, 'wb') as f:
                pickle.dump(spider.state, f, protocol=4)

    def spider_opened(self, spider: Spider) -> None:
        if self.jobdir and os.path.exists(self.statefn):
            with open(self.statefn, 'rb') as f:
                spider.state = pickle.load(f)
        else:
            spider.state = {}

    @property
    def statefn(self) -> str:
        return os.path.join(self.jobdir, 'spider.state')
