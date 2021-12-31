from w3lib.url import file_uri_to_path

from scrapy.responsetypes import responsetypes
from scrapy.utils.decorators import defers
from scrapy.http.request import Request
from scrapy.http.response.text import TextResponse
from scrapy.spiders import Spider


class FileDownloadHandler:
    lazy = False

    @defers
    def download_request(self, request: Request, spider: Spider) -> TextResponse:
        filepath = file_uri_to_path(request.url)
        with open(filepath, 'rb') as fo:
            body = fo.read()
        respcls = responsetypes.from_args(filename=filepath, body=body)
        return respcls(url=request.url, body=body)
