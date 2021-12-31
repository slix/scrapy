from scrapy.http.request import Request
from scrapy.item import Item
from tests.test_contracts import TestItem
from tests.test_engine import (
    AttrsItem,
    TestItem,
)
from typing import (
    Any,
    Dict,
    Iterator,
    List,
    Tuple,
    Union,
)


def iterate_spider_output(
    result: object
) -> Union[List[TestItem], List[Dict[str, List[str]]], List[Any], Tuple[()], List[TestItem], Iterator[Any], List[Request], List[Dict[Any, Any]], List[Item], List[AttrsItem], List[Dict[str, int]], List[Dict[str, str]], List[object], List[Union[Dict[str, int], Request]]]: ...
