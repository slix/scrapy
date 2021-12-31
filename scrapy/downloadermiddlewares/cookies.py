import logging
from collections import defaultdict

from scrapy.exceptions import NotConfigured
from scrapy.http import Response
from scrapy.http.cookies import CookieJar
from scrapy.utils.python import to_unicode
from http.cookiejar import Cookie
from scrapy.crawler import Crawler
from scrapy.http.request import Request
from scrapy.http.response import Response
from scrapy.spiders import Spider
from typing import Any, Dict, List, Optional, Union


logger = logging.getLogger(__name__)


class CookiesMiddleware:
    """This middleware enables working with sites that need cookies"""

    def __init__(self, debug: bool=False) -> None:
        self.jars = defaultdict(CookieJar)
        self.debug = debug

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> CookiesMiddleware:
        if not crawler.settings.getbool('COOKIES_ENABLED'):
            raise NotConfigured
        return cls(crawler.settings.getbool('COOKIES_DEBUG'))

    def process_request(self, request: Request, spider: Optional[Spider]) -> None:
        if request.meta.get('dont_merge_cookies', False):
            return

        cookiejarkey = request.meta.get("cookiejar")
        jar = self.jars[cookiejarkey]
        for cookie in self._get_request_cookies(jar, request):
            jar.set_cookie_if_ok(cookie, request)

        # set Cookie header
        request.headers.pop('Cookie', None)
        jar.add_cookie_header(request)
        self._debug_cookie(request, spider)

    def process_response(self, request: Request, response: Response, spider: Optional[Spider]) -> Response:
        if request.meta.get('dont_merge_cookies', False):
            return response

        # extract cookies from Set-Cookie and drop invalid/expired cookies
        cookiejarkey = request.meta.get("cookiejar")
        jar = self.jars[cookiejarkey]
        jar.extract_cookies(response, request)
        self._debug_set_cookie(response, spider)

        return response

    def _debug_cookie(self, request: Request, spider: Optional[Spider]) -> None:
        if self.debug:
            cl = [to_unicode(c, errors='replace')
                  for c in request.headers.getlist('Cookie')]
            if cl:
                cookies = "\n".join(f"Cookie: {c}\n" for c in cl)
                msg = f"Sending cookies to: {request}\n{cookies}"
                logger.debug(msg, extra={'spider': spider})

    def _debug_set_cookie(self, response: Response, spider: Optional[Spider]) -> None:
        if self.debug:
            cl = [to_unicode(c, errors='replace')
                  for c in response.headers.getlist('Set-Cookie')]
            if cl:
                cookies = "\n".join(f"Set-Cookie: {c}\n" for c in cl)
                msg = f"Received cookies from: {response}\n{cookies}"
                logger.debug(msg, extra={'spider': spider})

    def _format_cookie(self, cookie: Union[Dict[str, str], Dict[str, Union[float, str]], Dict[str, Union[bytes, str]], Dict[str, Union[str, int]], Dict[str, Optional[str]], Dict[str, Union[str, bool]]], request: Request) -> Optional[str]:
        """
        Given a dict consisting of cookie components, return its string representation.
        Decode from bytes if necessary.
        """
        decoded = {}
        for key in ("name", "value", "path", "domain"):
            if cookie.get(key) is None:
                if key in ("name", "value"):
                    msg = "Invalid cookie found in request {}: {} ('{}' is missing)"
                    logger.warning(msg.format(request, cookie, key))
                    return
                continue
            if isinstance(cookie[key], (bool, float, int, str)):
                decoded[key] = str(cookie[key])
            else:
                try:
                    decoded[key] = cookie[key].decode("utf8")
                except UnicodeDecodeError:
                    logger.warning("Non UTF-8 encoded cookie found in request %s: %s",
                                   request, cookie)
                    decoded[key] = cookie[key].decode("latin1", errors="replace")

        cookie_str = f"{decoded.pop('name')}={decoded.pop('value')}"
        for key, value in decoded.items():  # path, domain
            cookie_str += f"; {key.capitalize()}={value}"
        return cookie_str

    def _get_request_cookies(self, jar: CookieJar, request: Request) -> List[Union[Any, Cookie]]:
        """
        Extract cookies from the Request.cookies attribute
        """
        if not request.cookies:
            return []
        elif isinstance(request.cookies, dict):
            cookies = ({"name": k, "value": v} for k, v in request.cookies.items())
        else:
            cookies = request.cookies
        formatted = filter(None, (self._format_cookie(c, request) for c in cookies))
        response = Response(request.url, headers={"Set-Cookie": formatted})
        return jar.make_cookies(response, request)
