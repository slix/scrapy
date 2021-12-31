"""
This module contains data types used by Scrapy which are not included in the
Python Standard Library.

This module must not depend on any module outside the Standard Library.
"""

import collections
import weakref
from collections.abc import Mapping
from scrapy.http.request import Request
from typing import Any, Callable, Dict, Iterator, List, Optional, Set, Tuple, Union


class CaselessDict(dict):

    __slots__ = ()

    def __init__(self, seq: Optional[Union[List[Tuple[str, bytes]], Dict[str, List[str]], Dict[Any, Any], Dict[str, str], Dict[str, Union[str, List[str]]], Dict[bytes, List[bytes]], Dict[bytes, str], Dict[str, object], Dict[bytes, bytes], CaselessDict, Iterator[Any], Dict[str, None], Dict[str, Union[str, int]], Dict[str, bytes], Dict[str, filter], Dict[str, Union[bytes, int]], List[Union[Tuple[str, str], Tuple[str, bytes]]], List[Tuple[str, str]], Dict[str, int], Tuple[Tuple[str, int], Tuple[str, int]]]]=None) -> None:
        super().__init__()
        if seq:
            self.update(seq)

    def __getitem__(self, key: Union[bytes, str]) -> Optional[Union[List[Any], int, List[bytes], str]]:
        return dict.__getitem__(self, self.normkey(key))

    def __setitem__(self, key: Union[bytes, str], value: object) -> None:
        dict.__setitem__(self, self.normkey(key), self.normvalue(value))

    def __delitem__(self, key: str) -> None:
        dict.__delitem__(self, self.normkey(key))

    def __contains__(self, key: Union[bytes, str]) -> bool:
        return dict.__contains__(self, self.normkey(key))
    has_key = __contains__

    def __copy__(self) -> CaselessDict:
        return self.__class__(self)
    copy = __copy__

    def normkey(self, key: str) -> str:
        """Method to normalize dictionary key access"""
        return key.lower()

    def normvalue(self, value: Optional[Union[int, str]]) -> Optional[Union[int, str]]:
        """Method to normalize values prior to be set"""
        return value

    def get(self, key: Union[bytes, str], def_val: Optional[Union[int, bytes, str]]=None) -> Union[List[Any], str, int, List[bytes]]:
        return dict.get(self, self.normkey(key), self.normvalue(def_val))

    def setdefault(self, key: Union[bytes, str], def_val: object=None) -> Union[List[Any], int, List[bytes]]:
        return dict.setdefault(self, self.normkey(key), self.normvalue(def_val))

    def update(self, seq: Union[Dict[str, int], Dict[str, bytes], List[Tuple[str, bytes]], Dict[str, str], Dict[str, Union[str, int]], Dict[str, object], Tuple[Tuple[str, int], Tuple[str, int]], Dict[bytes, bytes], Dict[str, Union[str, List[str]]], Dict[str, filter], Dict[str, List[str]], Dict[str, Union[bytes, int]], List[Union[Tuple[str, str], Tuple[str, bytes]]], Iterator[Any], CaselessDict, Dict[bytes, List[bytes]], Dict[str, None], List[Tuple[str, str]], Dict[bytes, str]]) -> None:
        seq = seq.items() if isinstance(seq, Mapping) else seq
        iseq = ((self.normkey(k), self.normvalue(v)) for k, v in seq)
        super().update(iseq)

    @classmethod
    def fromkeys(cls, keys: Tuple[str, str], value: Optional[int]=None) -> CaselessDict:
        return cls((k, value) for k in keys)

    def pop(self, key: str, *args) -> Optional[Union[int, List[bytes]]]:
        return dict.pop(self, self.normkey(key), *args)


class LocalCache(collections.OrderedDict):
    """Dictionary with a finite number of keys.

    Older items expires first.
    """

    def __init__(self, limit: Optional[int]=None) -> None:
        super().__init__()
        self.limit = limit

    def __setitem__(self, key: str, value: int) -> None:
        if self.limit:
            while len(self) >= self.limit:
                self.popitem(last=False)
        super().__setitem__(key, value)


class LocalWeakReferencedCache(weakref.WeakKeyDictionary):
    """
    A weakref.WeakKeyDictionary implementation that uses LocalCache as its
    underlying data structure, making it ordered and capable of being size-limited.

    Useful for memoization, while avoiding keeping received
    arguments in memory only because of the cached references.

    Note: like LocalCache and unlike weakref.WeakKeyDictionary,
    it cannot be instantiated with an initial dictionary.
    """

    def __init__(self, limit: Optional[int]=None) -> None:
        super().__init__()
        self.data = LocalCache(limit=limit)

    def __setitem__(self, key: Optional[Union[int, Request, Callable, List[int]]], value: int) -> None:
        try:
            super().__setitem__(key, value)
        except TypeError:
            pass  # key is not weak-referenceable, skip caching

    def __getitem__(self, key: Optional[Union[Callable, Request]]) -> Optional[int]:
        try:
            return super().__getitem__(key)
        except (TypeError, KeyError):
            return None  # key is either not weak-referenceable or not cached


class SequenceExclude:
    """Object to test if an item is NOT within some sequence."""

    def __init__(self, seq: Union[Set[Union[float, int, str]], Set[str], range, str, List[int]]) -> None:
        self.seq = seq

    def __contains__(self, item: Union[float, List[str], Set[str], Tuple[int, int, int], int, str]) -> bool:
        return item not in self.seq
