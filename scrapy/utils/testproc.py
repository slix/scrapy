import sys
import os

from twisted.internet import defer, protocol
from twisted.internet.defer import Deferred
from twisted.python.failure import Failure
from typing import Any, List, Tuple, Union


class ProcessTest:

    command = None
    prefix = [sys.executable, '-m', 'scrapy.cmdline']
    cwd = os.getcwd()  # trial chdirs to temp dir

    def execute(self, args: List[Union[Any, str]], check_code: bool=True, settings: None=None) -> Deferred:
        from twisted.internet import reactor
        env = os.environ.copy()
        if settings is not None:
            env['SCRAPY_SETTINGS_MODULE'] = settings
        cmd = self.prefix + [self.command] + list(args)
        pp = TestProcessProtocol()
        pp.deferred.addBoth(self._process_finished, cmd, check_code)
        reactor.spawnProcess(pp, cmd[0], cmd, env=env, path=self.cwd)
        return pp.deferred

    def _process_finished(self, pp: TestProcessProtocol, cmd: List[str], check_code: bool) -> Tuple[int, bytes, bytes]:
        if pp.exitcode and check_code:
            msg = f"process {cmd} exit with code {pp.exitcode}"
            msg += f"\n>>> stdout <<<\n{pp.out}"
            msg += "\n"
            msg += f"\n>>> stderr <<<\n{pp.err}"
            raise RuntimeError(msg)
        return pp.exitcode, pp.out, pp.err


class TestProcessProtocol(protocol.ProcessProtocol):

    def __init__(self) -> None:
        self.deferred = defer.Deferred()
        self.out = b''
        self.err = b''
        self.exitcode = None

    def outReceived(self, data: bytes) -> None:
        self.out += data

    def errReceived(self, data: bytes) -> None:
        self.err += data

    def processEnded(self, status: Failure) -> None:
        self.exitcode = status.value.exitCode
        self.deferred.callback(self)
