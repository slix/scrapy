from datetime import datetime
from scrapy.http.request import Request
from scrapy.http.response import Response
from tests.test_contracts import TestItem
from tests.test_engine import (
    AttrsItem,
    TestItem,
)
from tests.test_exporters import (
    CustomFieldItem,
    TestItem,
)
from tests.test_loader import (
    AttrsNameItem,
    FunctionProcessorItem,
    NameItem,
    NoInputReprocessingItem,
    TestItem,
    TestNestedItem,
)
from tests.test_loader_deprecated import (
    FunctionProcessorItem,
    NameItem,
    TestItem,
)
from tests.test_logformatter import CustomItem
from tests.test_pipeline_files import (
    FilesPipelineTestAttrsItem,
    FilesPipelineTestItem,
    ItemWithFiles,
)
from tests.test_pipeline_images import (
    ImagesPipelineTestAttrsItem,
    ImagesPipelineTestItem,
)
from tests.test_squeues import TestItem
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Tuple,
    Type,
    Union,
)


class BaseItem:
    @staticmethod
    def __new__(
        cls: Union[Type[BaseItem], Type[TestItem], Type[TestItem], Type[FunctionProcessorItem], Type[ImagesPipelineTestItem], Type[TestItem], Type[TestNestedItem], Type[NoInputReprocessingItem], Type[Item], Type[DictItem], Type[TestItem], Type[TestItem], Type[CustomItem], Type[NameItem], Type[FilesPipelineTestItem], Type[ItemWithFiles], Type[TestItem], Type[CustomFieldItem]],
        *args,
        **kwargs
    ) -> BaseItem: ...


class DictItem:
    def __getattr__(self, name: str): ...
    def __getitem__(
        self,
        key: str
    ) -> Union[List[str], List[int], Dict[str, str], List[TestItem], TestItem, List[Dict[str, Union[str, List[TestItem]]]], str, List[Union[Dict[str, str], Dict[str, Union[str, Dict[str, List[str]]]]]], Dict[str, Union[str, TestItem]], List[Dict[str, str]], Dict[str, Union[str, Dict[str, str]]]]: ...
    def __init__(self, *args, **kwargs) -> None: ...
    @staticmethod
    def __new__(
        cls: Union[Type[TestItem], Type[TestItem], Type[FunctionProcessorItem], Type[ImagesPipelineTestItem], Type[TestItem], Type[TestNestedItem], Type[NoInputReprocessingItem], Type[Item], Type[DictItem], Type[TestItem], Type[CustomItem], Type[TestItem], Type[NameItem], Type[FilesPipelineTestItem], Type[ItemWithFiles], Type[TestItem], Type[CustomFieldItem]],
        *args,
        **kwargs
    ) -> DictItem: ...
    def __repr__(self) -> str: ...
    def __setattr__(self, name: str, value: Dict[Any, Any]) -> None: ...
    def __setitem__(
        self,
        key: str,
        value: Union[List[str], List[int], Dict[str, str], List[TestItem], TestItem, List[Dict[str, Union[str, List[TestItem]]]], List[Union[Dict[str, str], Dict[str, Union[str, Dict[str, List[str]]]]]], str, Dict[str, Union[str, TestItem]], List[Dict[str, str]], Tuple[str], Dict[str, Union[str, Dict[str, str]]]]
    ) -> None: ...


class ItemMeta:
    @staticmethod
    def __new__(
        mcs: Type[ItemMeta],
        class_name: str,
        bases: Union[Tuple[Type[DictItem]], Tuple[Type[NameItem]], Tuple[Type[Item]], Tuple[Type[NameItem]]],
        attrs: Union[Dict[str, str], Dict[str, Union[str, Field, Callable]], Dict[str, Union[str, Field]]]
    ) -> Union[Type[TestItem], Type[TestItem], Type[FunctionProcessorItem], Type[ImagesPipelineTestItem], Type[TestItem], Type[TestNestedItem], Type[FunctionProcessorItem], Type[NoInputReprocessingItem], Type[NameItem], Type[Item], Type[CustomItem], Type[TestItem], Type[TestItem], Type[NameItem], Type[FilesPipelineTestItem], Type[ItemWithFiles], Type[TestItem], Type[CustomFieldItem]]: ...


class _BaseItemMeta:
    def __instancecheck__(
        cls,
        instance: Union[Dict[str, Union[str, float]], AttrsItem, ImagesPipelineTestAttrsItem, float, Request, AttrsNameItem, Dict[str, Union[str, List[str], List[Dict[str, str]]]], Dict[str, Union[str, List[TestItem]]], Dict[str, Union[List[str], str]], FilesPipelineTestAttrsItem, List[Dict[str, int]], List[str], List[int], Dict[Any, Any], Dict[str, str], Dict[str, int], datetime, str, Dict[str, List[str]], Dict[str, Union[int, datetime, float]], Item, bytes, Dict[str, Union[int, float]], List[TestItem], int, Dict[str, bytes], List[Dict[str, Union[str, List[TestItem]]]], Dict[str, List[Union[Any, str]]], Response, Dict[str, Union[str, TestItem]], Dict[str, Union[str, List[int]]]]
    ) -> bool: ...
