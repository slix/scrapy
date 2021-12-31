from scrapy.http.response import Response
from scrapy.selector.unified import (
    Selector,
    SelectorList,
)
from tests.test_loader import (
    AttrsNameItem,
    NameItem,
    NestedItemLoader,
    NoInputReprocessingItem,
    TestNestedItem,
)
from tests.test_loader_deprecated import TestItem
from typing import (
    Dict,
    List,
    Optional,
    Union,
)


class ItemLoader:
    def __init__(
        self,
        item: Optional[Union[NoInputReprocessingItem, Dict[str, str], NameItem, TestItem, AttrsNameItem, Dict[str, List[str]], TestNestedItem]] = ...,
        selector: Optional[Union[Selector, SelectorList]] = ...,
        response: Optional[Response] = ...,
        parent: Optional[NestedItemLoader] = ...,
        **context
    ) -> None: ...
