import asyncio
from contextlib import suppress

from twisted.internet import asyncioreactor, error

from scrapy.utils.misc import load_object
from scrapy.extensions.telnet import TelnetConsole
from twisted.internet.tcp import Port
from typing import Callable, List


def listen_tcp(portrange: List[int], host: str, factory: TelnetConsole) -> Port:
    """Like reactor.listenTCP but tries different ports in a range."""
    from twisted.internet import reactor
    if len(portrange) > 2:
        raise ValueError(f"invalid portrange: {portrange}")
    if not portrange:
        return reactor.listenTCP(0, factory, interface=host)
    if not hasattr(portrange, '__iter__'):
        return reactor.listenTCP(portrange, factory, interface=host)
    if len(portrange) == 1:
        return reactor.listenTCP(portrange[0], factory, interface=host)
    for x in range(portrange[0], portrange[1] + 1):
        try:
            return reactor.listenTCP(x, factory, interface=host)
        except error.CannotListenError:
            if x == portrange[1]:
                raise


class CallLaterOnce:
    """Schedule a function to be called in the next reactor loop, but only if
    it hasn't been already scheduled since the last time it ran.
    """

    def __init__(self, func: Callable, *a, **kw) -> None:
        self._func = func
        self._a = a
        self._kw = kw
        self._call = None

    def schedule(self, delay: int=0) -> None:
        from twisted.internet import reactor
        if self._call is None:
            self._call = reactor.callLater(delay, self)

    def cancel(self) -> None:
        if self._call:
            self._call.cancel()

    def __call__(self) -> None:
        self._call = None
        return self._func(*self._a, **self._kw)


def install_reactor(reactor_path: str, event_loop_path: None=None) -> None:
    """Installs the :mod:`~twisted.internet.reactor` with the specified
    import path. Also installs the asyncio event loop with the specified import
    path if the asyncio reactor is enabled"""
    reactor_class = load_object(reactor_path)
    if reactor_class is asyncioreactor.AsyncioSelectorReactor:
        with suppress(error.ReactorAlreadyInstalledError):
            if event_loop_path is not None:
                event_loop_class = load_object(event_loop_path)
                event_loop = event_loop_class()
                asyncio.set_event_loop(event_loop)
            else:
                event_loop = asyncio.get_event_loop()
            asyncioreactor.install(eventloop=event_loop)
    else:
        *module, _ = reactor_path.split(".")
        installer_path = module + ["install"]
        installer = load_object(".".join(installer_path))
        with suppress(error.ReactorAlreadyInstalledError):
            installer()


def verify_installed_reactor(reactor_path: str) -> None:
    """Raises :exc:`Exception` if the installed
    :mod:`~twisted.internet.reactor` does not match the specified import
    path."""
    from twisted.internet import reactor
    reactor_class = load_object(reactor_path)
    if not isinstance(reactor, reactor_class):
        msg = ("The installed reactor "
               f"({reactor.__module__}.{reactor.__class__.__name__}) does not "
               f"match the requested one ({reactor_path})")
        raise Exception(msg)


def is_asyncio_reactor_installed() -> bool:
    from twisted.internet import reactor
    return isinstance(reactor, asyncioreactor.AsyncioSelectorReactor)
