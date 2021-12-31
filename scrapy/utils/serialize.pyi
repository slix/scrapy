from datetime import (
    date,
    datetime,
    time,
)
from decimal import Decimal
from scrapy.http.request import Request
from scrapy.http.response import Response
from tests.test_exporters import TestItem
from twisted.internet.defer import Deferred
from typing import (
    Dict,
    List,
    Set,
    Union,
)


class ScrapyJSONEncoder:
    def default(
        self,
        o: Union[TestItem, Set[str], Deferred, date, Response, Decimal, Request, Set[datetime], time]
    ) -> Union[Dict[str, str], List[str], Dict[str, Union[str, Dict[str, str]]], str, List[datetime]]: ...
