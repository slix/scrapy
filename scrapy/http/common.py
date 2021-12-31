from typing import Callable

def obsolete_setter(setter: Callable, attrname: str) -> Callable:
    def newsetter(self, value):
        c = self.__class__.__name__
        msg = f"{c}.{attrname} is not modifiable, use {c}.replace() instead"
        raise AttributeError(msg)
    return newsetter
