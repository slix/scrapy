from w3lib.http import headers_dict_to_raw
from scrapy.utils.datatypes import CaselessDict
from scrapy.utils.python import to_unicode
from typing import Any, Dict, Iterator, List, Optional, Tuple, Union


class Headers(CaselessDict):
    """Case insensitive http headers dictionary"""

    def __init__(self, seq: Optional[Union[Dict[str, None], Dict[str, List[str]], List[Tuple[str, str]], List[Union[Tuple[str, str], Tuple[str, bytes]]], Dict[str, bytes], Dict[bytes, str], Dict[str, int], Dict[str, Union[str, List[str]]], Dict[str, Union[bytes, int]], Dict[bytes, List[bytes]], Dict[str, object], Dict[str, filter], Dict[str, str], List[Tuple[str, bytes]], Dict[str, Union[str, int]], Dict[bytes, bytes], Dict[Any, Any], Headers]]=None, encoding: str='utf-8') -> None:
        self.encoding = encoding
        super().__init__(seq)

    def normkey(self, key: Union[bytes, str]) -> bytes:
        """Normalize key to bytes"""
        return self._tobytes(key.title())

    def normvalue(self, value: object) -> List[Union[Any, bytes]]:
        """Normalize values to bytes"""
        if value is None:
            value = []
        elif isinstance(value, (str, bytes)):
            value = [value]
        elif not hasattr(value, '__iter__'):
            value = [value]

        return [self._tobytes(x) for x in value]

    def _tobytes(self, x: object) -> bytes:
        if isinstance(x, bytes):
            return x
        elif isinstance(x, str):
            return x.encode(self.encoding)
        elif isinstance(x, int):
            return str(x).encode(self.encoding)
        else:
            raise TypeError(f'Unsupported value type: {type(x)}')

    def __getitem__(self, key: Union[bytes, str]) -> bytes:
        try:
            return super().__getitem__(key)[-1]
        except IndexError:
            return None

    def get(self, key: Union[bytes, str], def_val: Optional[Union[bytes, int, str]]=None) -> Optional[bytes]:
        try:
            return super().get(key, def_val)[-1]
        except IndexError:
            return None

    def getlist(self, key: Union[bytes, str], def_val: Optional[Union[List[str], str]]=None) -> List[Union[Any, bytes]]:
        try:
            return super().__getitem__(key)
        except KeyError:
            if def_val is not None:
                return self.normvalue(def_val)
            return []

    def setlist(self, key: str, list_: List[object]) -> None:
        self[key] = list_

    def setlistdefault(self, key: str, default_list: List[str]=()) -> List[bytes]:
        return self.setdefault(key, default_list)

    def appendlist(self, key: Union[bytes, str], value: Union[bytes, str]) -> None:
        lst = self.getlist(key)
        lst.extend(self.normvalue(value))
        self[key] = lst

    def items(self) -> Iterator[Any]:
        return ((k, self.getlist(k)) for k in self.keys())

    def values(self) -> List[bytes]:
        return [self[k] for k in self.keys()]

    def to_string(self) -> bytes:
        return headers_dict_to_raw(self)

    def to_unicode_dict(self) -> CaselessDict:
        """ Return headers as a CaselessDict with unicode keys
        and unicode values. Multiple values are joined with ','.
        """
        return CaselessDict(
            (to_unicode(key, encoding=self.encoding),
             to_unicode(b','.join(value), encoding=self.encoding))
            for key, value in self.items())

    def __copy__(self) -> Headers:
        return self.__class__(self)
    copy = __copy__
