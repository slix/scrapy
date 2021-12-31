"""Set User-Agent header per spider or use a default value from settings"""

from scrapy import signals
from scrapy.crawler import Crawler
from scrapy.http.request import Request
from scrapy.spiders import Spider
from typing import Optional


class UserAgentMiddleware:
    """This middleware allows spiders to override the user_agent"""

    def __init__(self, user_agent: Optional[str]='Scrapy') -> None:
        self.user_agent = user_agent

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> UserAgentMiddleware:
        o = cls(crawler.settings['USER_AGENT'])
        crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        return o

    def spider_opened(self, spider: Spider) -> None:
        self.user_agent = getattr(spider, 'user_agent', self.user_agent)

    def process_request(self, request: Request, spider: Spider) -> None:
        if self.user_agent:
            request.headers.setdefault(b'User-Agent', self.user_agent)
