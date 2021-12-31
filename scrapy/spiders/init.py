from scrapy.spiders import Spider
from scrapy.utils.spider import iterate_spider_output
from typing import Any, Iterator


class InitSpider(Spider):
    """Base Spider with initialization facilities"""

    def start_requests(self) -> Iterator[Any]:
        self._postinit_reqs = super().start_requests()
        return iterate_spider_output(self.init_request())

    def initialized(self, response: None=None) -> Iterator[Any]:
        """This method must be set as the callback of your last initialization
        request. See self.init_request() docstring for more info.
        """
        return self.__dict__.pop('_postinit_reqs')

    def init_request(self) -> Iterator[Any]:
        """This function should return one initialization request, with the
        self.initialized method as callback. When the self.initialized method
        is called this spider is considered initialized. If you need to perform
        several requests for initializing your spider, you can do so by using
        different callbacks. The only requirement is that the final callback
        (of the last initialization request) must be self.initialized.

        The default implementation calls self.initialized immediately, and
        means that no initialization is needed. This method should be
        overridden only when you need to perform requests to initialize your
        spider
        """
        return self.initialized()
