import json
import copy
from collections.abc import MutableMapping
from importlib import import_module
from pprint import pformat

from scrapy.settings import default_settings
from typing import Any, Dict, Iterator, List, Optional, Tuple, Type, Union


SETTINGS_PRIORITIES = {
    'default': 0,
    'command': 10,
    'project': 20,
    'spider': 30,
    'cmdline': 40,
}


def get_settings_priority(priority: Union[int, str]) -> int:
    """
    Small helper function that looks up a given string priority in the
    :attr:`~scrapy.settings.SETTINGS_PRIORITIES` dictionary and returns its
    numerical value, or directly returns a given numerical priority.
    """
    if isinstance(priority, str):
        return SETTINGS_PRIORITIES[priority]
    else:
        return priority


class SettingsAttribute:

    """Class for storing data related to settings attributes.

    This class is intended for internal usage, you should try Settings class
    for settings configuration, not this one.
    """

    def __init__(self, value: Optional[Union[Type[FileDownloadHandler], float, Type[FromCrawlerCsvItemExporter], Type[FTPFeedStorageWithoutFeedOptions], Type[FTPFeedStorageWithoutFeedOptionsWithFromCrawler], Type[DummyBlockingFeedStorage], Dict[str, Union[str, List[Union[Type[FeedPostProcessedExportsTest.MyPlugin1], str]], bytes]], Type[DummyLazyDH], Dict[str, Union[str, List[str], int]], Dict[str, Tuple[int, int]], Type[FromCrawlerFileFeedStorage], Dict[str, str], Dict[str, Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]], bytes]], Dict[str, Optional[str]], Dict[Any, Any], BaseSettings, Type[OffDH], Type[DummyDH], Dict[str, Optional[Union[str, List[str]]]], Type[S3FeedStorageWithoutFeedOptions], Dict[str, Optional[Union[str, int]]], Type[StdoutFeedStorageWithoutFeedOptions], Dict[str, Union[str, List[str]]], Type[FileFeedStorageWithoutFeedOptions], List[int], str, Type[S3FeedStorageWithoutFeedOptionsWithFromCrawler], List[str], List[List[str]], List[Any], Tuple[int], Type[LogOnStoreFileStorage], int, Dict[str, Union[str, Dict[str, bool]]], Dict[str, Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]]]], Dict[str, Union[str, List[str], List[Dict[str, int]]]], Dict[str, Union[str, int]], Type[FailingBlockingFeedStorage], Dict[str, int]]], priority: int) -> None:
        self.value = value
        if isinstance(self.value, BaseSettings):
            self.priority = max(self.value.maxpriority(), priority)
        else:
            self.priority = priority

    def set(self, value: Optional[Union[Dict[str, Type[OffDH]], Dict[str, Dict[str, Union[str, List[Union[Type[FeedPostProcessedExportsTest.MyPlugin1], str]], bytes]]], float, Type[FromCrawlerCsvItemExporter], Dict[Type[InjectArgumentsSpiderMiddleware], int], Dict[str, Type[FTPFeedStorageWithoutFeedOptionsWithFromCrawler]], Dict[Type[SimplePipeline], int], Type[FTPFeedStorageWithoutFeedOptions], Type[FTPFeedStorageWithoutFeedOptionsWithFromCrawler], Type[DummyBlockingFeedStorage], Dict[str, Type[FTPFeedStorageWithoutFeedOptions]], Dict[str, Type[DummyBlockingFeedStorage]], Dict[str, Union[Dict[str, Union[str, List[str], int]], Dict[str, Optional[Union[str, List[str]]]]]], Dict[Union[Type[NotGeneratorFailMiddleware], Type[NotGeneratorDoNothingAfterFailureMiddleware], Type[NotGeneratorRecoverMiddleware], Type[NotGeneratorDoNothingAfterRecoveryMiddleware]], int], Dict[Union[Type[RaiseExceptionRequestMiddleware], Type[CatchExceptionDoNotOverrideRequestMiddleware]], int], Dict[Type[AsyncDefNotAsyncioPipeline], int], Dict[str, Type[StdoutFeedStorageWithoutFeedOptions]], Tuple[int, int, int, int], Dict[Type[AsyncDefPipeline], int], Dict[Type[ProcessResponseMiddleware], int], Dict[str, Type[S3FeedStorageWithoutFeedOptionsWithFromCrawler]], Dict[str, Type[FailingBlockingFeedStorage]], Type[FromCrawlerFileFeedStorage], Dict[Any, Any], Dict[str, str], Dict[str, Dict[str, Union[str, List[str], int]]], Type[SimpleScheduler], BaseSettings, Dict[Type[InjectArgumentsDownloaderMiddleware], int], Dict[str, Dict[str, Optional[Union[str, int]]]], Dict[Union[Type[FailProcessSpiderInputMiddleware], Type[LogExceptionMiddleware]], int], Type[SpiderLoaderWithWrongInterface], Dict[str, Type[S3FeedStorageWithoutFeedOptions]], Dict[Type[AsyncDefAsyncioPipeline], int], Dict[Union[Type[RaiseExceptionRequestMiddleware], Type[CatchExceptionOverrideRequestMiddleware]], int], Type[S3FeedStorageWithoutFeedOptions], Type[SkipMessagesLogFormatter], Type[MinimalScheduler], Type[StdoutFeedStorageWithoutFeedOptions], Dict[str, Dict[str, Optional[str]]], Dict[Union[Type[GeneratorFailMiddleware], Type[GeneratorDoNothingAfterFailureMiddleware], Type[GeneratorRecoverMiddleware], Type[GeneratorDoNothingAfterRecoveryMiddleware]], int], Dict[str, Type[DummyDH]], Dict[Type[DeferredPipeline], int], Dict[str, Type[FileFeedStorageWithoutFeedOptions]], Dict[str, Dict[str, Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]], bytes]]], Type[FailingBlockingFeedStorage], Type[FileFeedStorageWithoutFeedOptions], Dict[Type[LogExceptionMiddleware], int], Dict[str, Dict[Any, Any]], Dict[str, Dict[str, str]], str, List[str], Dict[str, Dict[str, Union[str, List[str]]]], Dict[str, Type[FromCrawlerCsvItemExporter]], Type[S3FeedStorageWithoutFeedOptionsWithFromCrawler], Dict[str, Type[LogOnStoreFileStorage]], List[Any], List[int], Dict[str, Dict[str, Union[str, int]]], Type[DirectDupeFilter], Type[LogOnStoreFileStorage], Dict[Type[RecoveryMiddleware], int], Dict[str, Dict[str, Union[str, List[str], List[Dict[str, int]]]]], Type[CustomPythonOrgPolicy], Type[FromCrawlerRFPDupeFilter], Dict[str, Type[DummyLazyDH]], int, Dict[str, Type[FileDownloadHandler]], Type[FromSettingsRFPDupeFilter], Dict[str, Type[FromCrawlerFileFeedStorage]], Dict[str, Dict[str, Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]]]]], Dict[str, Dict[str, Union[str, Dict[str, bool]]]], Dict[str, None], Dict[Type[AlternativeCallbacksMiddleware], int], Dict[Type[RaiseExceptionRequestMiddleware], int], Dict[Type[DropSomeItemsPipeline], int], Dict[str, int]]], priority: int) -> None:
        """Sets value if priority is higher or equal than current priority."""
        if priority >= self.priority:
            if isinstance(self.value, BaseSettings):
                value = BaseSettings(value, priority=priority)
            self.value = value
            self.priority = priority

    def __str__(self) -> str:
        return f"<SettingsAttribute value={self.value!r} priority={self.priority}>"

    __repr__ = __str__


class BaseSettings(MutableMapping):
    """
    Instances of this class behave like dictionaries, but store priorities
    along with their ``(key, value)`` pairs, and can be frozen (i.e. marked
    immutable).

    Key-value entries can be passed on initialization with the ``values``
    argument, and they would take the ``priority`` level (unless ``values`` is
    already an instance of :class:`~scrapy.settings.BaseSettings`, in which
    case the existing priority levels will be kept).  If the ``priority``
    argument is a string, the priority name will be looked up in
    :attr:`~scrapy.settings.SETTINGS_PRIORITIES`. Otherwise, a specific integer
    should be provided.

    Once the object is created, new settings can be loaded or updated with the
    :meth:`~scrapy.settings.BaseSettings.set` method, and can be accessed with
    the square bracket notation of dictionaries, or with the
    :meth:`~scrapy.settings.BaseSettings.get` method of the instance and its
    value conversion variants. When requesting a stored key, the value with the
    highest priority will be retrieved.
    """

    def __init__(self, values: Optional[Union[Dict[str, Type[OffDH]], Dict[str, Dict[str, Union[str, List[Union[Type[FeedPostProcessedExportsTest.MyPlugin1], str]], bytes]]], Dict[Type[InjectArgumentsSpiderMiddleware], int], Dict[str, Type[FTPFeedStorageWithoutFeedOptionsWithFromCrawler]], Dict[Type[SimplePipeline], int], Dict[str, Type[FTPFeedStorageWithoutFeedOptions]], Dict[str, Type[DummyBlockingFeedStorage]], Dict[str, Union[str, List[int], bool, BaseSettings]], Dict[Union[Type[NotGeneratorFailMiddleware], Type[NotGeneratorDoNothingAfterFailureMiddleware], Type[NotGeneratorRecoverMiddleware], Type[NotGeneratorDoNothingAfterRecoveryMiddleware]], int], Dict[Type[AsyncDefNotAsyncioPipeline], int], Dict[Union[Type[RaiseExceptionRequestMiddleware], Type[CatchExceptionDoNotOverrideRequestMiddleware]], int], Dict[Type[ProcessResponseMiddleware], int], Dict[Type[AsyncDefPipeline], int], Dict[str, Type[S3FeedStorageWithoutFeedOptionsWithFromCrawler]], Dict[str, Type[StdoutFeedStorageWithoutFeedOptions]], Dict[str, Type[FailingBlockingFeedStorage]], Dict[str, None], Dict[str, Dict[str, Union[str, List[str], int]]], Dict[Any, Any], Dict[str, str], BaseSettings, Dict[Type[InjectArgumentsDownloaderMiddleware], int], Dict[str, Dict[str, Optional[Union[str, int]]]], Dict[Union[Type[FailProcessSpiderInputMiddleware], Type[LogExceptionMiddleware]], int], Dict[str, BaseSettings], Dict[str, Type[S3FeedStorageWithoutFeedOptions]], Dict[int, int], Dict[Type[AsyncDefAsyncioPipeline], int], Dict[Union[Type[RaiseExceptionRequestMiddleware], Type[CatchExceptionOverrideRequestMiddleware]], int], Dict[Type[DeferredPipeline], int], Dict[Union[Type[GeneratorFailMiddleware], Type[GeneratorDoNothingAfterFailureMiddleware], Type[GeneratorRecoverMiddleware], Type[GeneratorDoNothingAfterRecoveryMiddleware]], int], Dict[str, Dict[str, Optional[str]]], Dict[str, Type[DummyDH]], Dict[str, Type[FileFeedStorageWithoutFeedOptions]], Dict[str, Dict[str, Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]], bytes]]], Dict[Type[LogExceptionMiddleware], int], Dict[str, Dict[str, str]], Dict[str, Dict[Any, Any]], str, Dict[str, Type[LogOnStoreFileStorage]], Dict[str, Dict[str, Union[str, List[str]]]], Dict[str, Type[FromCrawlerCsvItemExporter]], Dict[str, Dict[str, Union[int, str]]], Dict[Type[RecoveryMiddleware], int], Dict[str, Dict[str, Union[str, List[str], List[Dict[str, int]]]]], Dict[str, Type[DummyLazyDH]], Dict[str, Union[int, BaseSettings]], Dict[str, Type[FileDownloadHandler]], Dict[str, Type[FromCrawlerFileFeedStorage]], Dict[str, Dict[str, Union[str, Dict[str, bool]]]], Dict[str, Dict[str, Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]]]]], Dict[str, Union[Dict[str, Union[str, List[str], int]], Dict[str, Optional[Union[str, List[str]]]]]], Dict[Type[AlternativeCallbacksMiddleware], int], Dict[Type[RaiseExceptionRequestMiddleware], int], Dict[Type[DropSomeItemsPipeline], int], Dict[str, int]]]=None, priority: Union[int, str]='project') -> None:
        self.frozen = False
        self.attributes = {}
        if values:
            self.update(values, priority)

    def __getitem__(self, opt_name: Union[Type[RecoveryMiddleware], Type[CatchExceptionDoNotOverrideRequestMiddleware], Type[GeneratorDoNothingAfterFailureMiddleware], Type[ProcessResponseMiddleware], Type[SimplePipeline], Type[GeneratorFailMiddleware], Type[DropSomeItemsPipeline], Type[InjectArgumentsSpiderMiddleware], Type[NotGeneratorDoNothingAfterRecoveryMiddleware], Type[AlternativeCallbacksMiddleware], Type[FailProcessSpiderInputMiddleware], str, Type[InjectArgumentsDownloaderMiddleware], Type[NotGeneratorFailMiddleware], Type[AsyncDefNotAsyncioPipeline], Type[NotGeneratorDoNothingAfterFailureMiddleware], Type[NotGeneratorRecoverMiddleware], Type[LogExceptionMiddleware], Type[GeneratorDoNothingAfterRecoveryMiddleware], Type[AsyncDefPipeline], int, Type[AsyncDefAsyncioPipeline], Type[GeneratorRecoverMiddleware], Type[RaiseExceptionRequestMiddleware], Type[CatchExceptionOverrideRequestMiddleware], Type[DeferredPipeline]]) -> Optional[Union[Type[FileDownloadHandler], Type[FromCrawlerCsvItemExporter], float, Type[FTPFeedStorageWithoutFeedOptions], Type[FTPFeedStorageWithoutFeedOptionsWithFromCrawler], Type[DummyBlockingFeedStorage], Dict[str, Union[str, List[Union[Type[FeedPostProcessedExportsTest.MyPlugin1], str]], bytes]], Type[DummyLazyDH], Dict[str, Union[str, List[str], int]], Dict[str, Tuple[int, int]], Tuple[int, int, int, int], Type[FromCrawlerFileFeedStorage], Dict[str, str], Type[SpiderLoaderWithWrongInterface], Dict[Any, Any], Type[SimpleScheduler], BaseSettings, Dict[str, Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]], bytes]], Dict[str, Optional[str]], Type[OffDH], Dict[str, Optional[Union[str, List[str]]]], Type[DummyDH], Type[S3FeedStorageWithoutFeedOptions], Type[SkipMessagesLogFormatter], Dict[str, Optional[Union[str, int]]], Type[StdoutFeedStorageWithoutFeedOptions], Type[MinimalScheduler], Dict[str, Union[str, List[str]]], Type[FileFeedStorageWithoutFeedOptions], List[int], List[str], Type[S3FeedStorageWithoutFeedOptionsWithFromCrawler], List[Any], str, List[List[str]], Type[DirectDupeFilter], Tuple[int], Type[LogOnStoreFileStorage], Type[CustomPythonOrgPolicy], Type[FromCrawlerRFPDupeFilter], int, Dict[str, Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]]]], Type[FromSettingsRFPDupeFilter], Dict[str, Union[str, List[str], List[Dict[str, int]]]], Dict[str, Union[int, str]], Dict[str, Union[str, Dict[str, bool]]], Type[FailingBlockingFeedStorage], Dict[str, int]]]:
        if opt_name not in self:
            return None
        return self.attributes[opt_name].value

    def __contains__(self, name: Union[Type[RecoveryMiddleware], Type[CatchExceptionDoNotOverrideRequestMiddleware], Type[GeneratorDoNothingAfterFailureMiddleware], Type[ProcessResponseMiddleware], Type[SimplePipeline], Type[GeneratorFailMiddleware], Type[DropSomeItemsPipeline], Type[InjectArgumentsSpiderMiddleware], Type[NotGeneratorDoNothingAfterRecoveryMiddleware], Type[AlternativeCallbacksMiddleware], Type[FailProcessSpiderInputMiddleware], str, Type[NotGeneratorFailMiddleware], Type[InjectArgumentsDownloaderMiddleware], Type[AsyncDefNotAsyncioPipeline], Type[NotGeneratorDoNothingAfterFailureMiddleware], Type[NotGeneratorRecoverMiddleware], Type[GeneratorDoNothingAfterRecoveryMiddleware], Type[LogExceptionMiddleware], Type[AsyncDefPipeline], int, Type[AsyncDefAsyncioPipeline], Type[GeneratorRecoverMiddleware], Type[RaiseExceptionRequestMiddleware], Type[CatchExceptionOverrideRequestMiddleware], Type[DeferredPipeline]]) -> bool:
        return name in self.attributes

    def get(self, name: str, default: Optional[Union[Dict[str, Tuple[int, int]], float, Dict[Any, Any], int, List[Any], str, List[str], Dict[str, int]]]=None) -> Optional[Union[Dict[str, Tuple[int, int]], Type[CustomPythonOrgPolicy], float, Dict[Any, Any], Type[SpiderLoaderWithWrongInterface], int, BaseSettings, Dict[str, Union[int, str]], List[int], str, List[Any], List[str], List[List[str]], Tuple[int], Dict[str, int]]]:
        """
        Get a setting value without affecting its original type.

        :param name: the setting name
        :type name: str

        :param default: the value to return if no setting is found
        :type default: object
        """
        return self[name] if self[name] is not None else default

    def getbool(self, name: str, default: bool=False) -> bool:
        """
        Get a setting value as a boolean.

        ``1``, ``'1'``, `True`` and ``'True'`` return ``True``,
        while ``0``, ``'0'``, ``False``, ``'False'`` and ``None`` return ``False``.

        For example, settings populated through environment variables set to
        ``'0'`` will return ``False`` when using this method.

        :param name: the setting name
        :type name: str

        :param default: the value to return if no setting is found
        :type default: object
        """
        got = self.get(name, default)
        try:
            return bool(int(got))
        except ValueError:
            if got in ("True", "true"):
                return True
            if got in ("False", "false"):
                return False
            raise ValueError("Supported values for boolean settings "
                             "are 0/1, True/False, '0'/'1', "
                             "'True'/'False' and 'true'/'false'")

    def getint(self, name: str, default: int=0) -> int:
        """
        Get a setting value as an int.

        :param name: the setting name
        :type name: str

        :param default: the value to return if no setting is found
        :type default: object
        """
        return int(self.get(name, default))

    def getfloat(self, name: str, default: float=0.0) -> float:
        """
        Get a setting value as a float.

        :param name: the setting name
        :type name: str

        :param default: the value to return if no setting is found
        :type default: object
        """
        return float(self.get(name, default))

    def getlist(self, name: str, default: Optional[List[str]]=None) -> List[Union[Any, int, str]]:
        """
        Get a setting value as a list. If the setting original type is a list, a
        copy of it will be returned. If it's a string it will be split by ",".

        For example, settings populated through environment variables set to
        ``'one,two'`` will return a list ['one', 'two'] when using this method.

        :param name: the setting name
        :type name: str

        :param default: the value to return if no setting is found
        :type default: object
        """
        value = self.get(name, default or [])
        if isinstance(value, str):
            value = value.split(',')
        return list(value)

    def getdict(self, name: str, default: Optional[Dict[str, int]]=None) -> Union[Dict[str, Dict[str, Union[str, List[Union[Type[FeedPostProcessedExportsTest.MyPlugin1], str]], bytes]]], Dict[str, Dict[str, Union[str, List[str], List[Dict[str, int]]]]], Dict[str, Dict[str, Optional[str]]], Dict[str, Dict[str, Union[str, List[str], int]]], Dict[Any, Any], Dict[str, str], Dict[str, Dict[str, Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]], bytes]]], Dict[str, Type[FileDownloadHandler]], Dict[str, Dict[str, Optional[Union[str, int]]]], Dict[str, Union[int, str]], Dict[str, Dict[str, Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]]]]], Dict[str, Dict[str, Union[str, Dict[str, bool]]]], Dict[str, Dict[str, str]], Dict[str, Dict[Any, Any]], Dict[str, Dict[str, Union[str, List[str]]]], Dict[str, Union[Dict[str, Union[str, List[str], int]], Dict[str, Optional[Union[str, List[str]]]]]], Dict[str, Dict[str, Union[int, str]]], Dict[str, int]]:
        """
        Get a setting value as a dictionary. If the setting original type is a
        dictionary, a copy of it will be returned. If it is a string it will be
        evaluated as a JSON dictionary. In the case that it is a
        :class:`~scrapy.settings.BaseSettings` instance itself, it will be
        converted to a dictionary, containing all its current settings values
        as they would be returned by :meth:`~scrapy.settings.BaseSettings.get`,
        and losing all information about priority and mutability.

        :param name: the setting name
        :type name: str

        :param default: the value to return if no setting is found
        :type default: object
        """
        value = self.get(name, default or {})
        if isinstance(value, str):
            value = json.loads(value)
        return dict(value)

    def getwithbase(self, name: str) -> BaseSettings:
        """Get a composition of a dictionary-like setting and its `_BASE`
        counterpart.

        :param name: name of the dictionary-like setting
        :type name: str
        """
        compbs = BaseSettings()
        compbs.update(self[name + '_BASE'])
        compbs.update(self[name])
        return compbs

    def getpriority(self, name: Union[Type[RecoveryMiddleware], Type[CatchExceptionDoNotOverrideRequestMiddleware], Type[GeneratorDoNothingAfterFailureMiddleware], Type[ProcessResponseMiddleware], Type[SimplePipeline], Type[GeneratorFailMiddleware], Type[DropSomeItemsPipeline], Type[InjectArgumentsSpiderMiddleware], Type[NotGeneratorDoNothingAfterRecoveryMiddleware], Type[AlternativeCallbacksMiddleware], Type[FailProcessSpiderInputMiddleware], str, Type[InjectArgumentsDownloaderMiddleware], Type[NotGeneratorFailMiddleware], Type[AsyncDefNotAsyncioPipeline], Type[NotGeneratorDoNothingAfterFailureMiddleware], Type[NotGeneratorRecoverMiddleware], Type[LogExceptionMiddleware], Type[GeneratorDoNothingAfterRecoveryMiddleware], Type[AsyncDefPipeline], int, Type[AsyncDefAsyncioPipeline], Type[GeneratorRecoverMiddleware], Type[RaiseExceptionRequestMiddleware], Type[CatchExceptionOverrideRequestMiddleware], Type[DeferredPipeline]]) -> Optional[int]:
        """
        Return the current numerical priority value of a setting, or ``None`` if
        the given ``name`` does not exist.

        :param name: the setting name
        :type name: str
        """
        if name not in self:
            return None
        return self.attributes[name].priority

    def maxpriority(self) -> int:
        """
        Return the numerical value of the highest priority present throughout
        all settings, or the numerical value for ``default`` from
        :attr:`~scrapy.settings.SETTINGS_PRIORITIES` if there are no settings
        stored.
        """
        if len(self) > 0:
            return max(self.getpriority(name) for name in self)
        else:
            return get_settings_priority('default')

    def __setitem__(self, name: str, value: Union[Dict[str, Dict[str, str]], str]) -> None:
        self.set(name, value)

    def set(self, name: Union[Type[RecoveryMiddleware], Type[CatchExceptionDoNotOverrideRequestMiddleware], Type[GeneratorDoNothingAfterFailureMiddleware], Type[ProcessResponseMiddleware], Type[SimplePipeline], Type[GeneratorFailMiddleware], Type[DropSomeItemsPipeline], Type[InjectArgumentsSpiderMiddleware], Type[NotGeneratorDoNothingAfterRecoveryMiddleware], Type[AlternativeCallbacksMiddleware], Type[FailProcessSpiderInputMiddleware], Type[NotGeneratorFailMiddleware], str, Type[InjectArgumentsDownloaderMiddleware], Type[AsyncDefNotAsyncioPipeline], Type[NotGeneratorDoNothingAfterFailureMiddleware], Type[NotGeneratorRecoverMiddleware], Type[GeneratorDoNothingAfterRecoveryMiddleware], Type[LogExceptionMiddleware], Type[AsyncDefPipeline], int, Type[AsyncDefAsyncioPipeline], Type[GeneratorRecoverMiddleware], Type[RaiseExceptionRequestMiddleware], Type[CatchExceptionOverrideRequestMiddleware], Type[DeferredPipeline]], value: Optional[Union[Dict[str, Type[OffDH]], Dict[str, Dict[str, Union[str, List[Union[Type[FeedPostProcessedExportsTest.MyPlugin1], str]], bytes]]], float, Dict[str, Type[FTPFeedStorageWithoutFeedOptions]], Dict[str, Type[StdoutFeedStorageWithoutFeedOptions]], Dict[str, Type[FailingBlockingFeedStorage]], Dict[str, Dict[str, Union[str, List[str], int]]], Dict[Any, Any], Dict[str, str], Dict[str, Type[S3FeedStorageWithoutFeedOptions]], Dict[Union[Type[RaiseExceptionRequestMiddleware], Type[CatchExceptionOverrideRequestMiddleware]], int], Dict[str, Type[DummyDH]], Type[FileFeedStorageWithoutFeedOptions], str, List[Any], List[List[str]], Dict[str, Dict[str, Union[str, List[str], List[Dict[str, int]]]]], Dict[str, Type[FileDownloadHandler]], Dict[str, Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]]]], Type[FromSettingsRFPDupeFilter], Dict[str, Dict[str, Union[str, Dict[str, bool]]]], Dict[str, None], Type[FileDownloadHandler], Dict[Type[SimplePipeline], int], Type[DummyBlockingFeedStorage], Dict[Union[Type[NotGeneratorFailMiddleware], Type[NotGeneratorDoNothingAfterFailureMiddleware], Type[NotGeneratorRecoverMiddleware], Type[NotGeneratorDoNothingAfterRecoveryMiddleware]], int], Dict[str, Union[str, List[str], int]], Tuple[int, int, int, int], Dict[str, Type[S3FeedStorageWithoutFeedOptionsWithFromCrawler]], Dict[str, Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]], bytes]], Dict[str, Optional[str]], Type[SpiderLoaderWithWrongInterface], BaseSettings, Dict[Type[InjectArgumentsDownloaderMiddleware], int], Type[S3FeedStorageWithoutFeedOptions], Type[SkipMessagesLogFormatter], Type[StdoutFeedStorageWithoutFeedOptions], Dict[str, Dict[str, Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]], bytes]]], Dict[Type[LogExceptionMiddleware], int], Dict[str, Type[LogOnStoreFileStorage]], List[str], Dict[str, Dict[str, Union[str, List[str]]]], Dict[Type[RecoveryMiddleware], int], Type[CustomPythonOrgPolicy], Dict[str, Union[Dict[str, Union[str, List[str], int]], Dict[str, Optional[Union[str, List[str]]]]]], Dict[Type[RaiseExceptionRequestMiddleware], int], Dict[str, int], Type[FromCrawlerCsvItemExporter], Type[FTPFeedStorageWithoutFeedOptions], Dict[str, Type[DummyBlockingFeedStorage]], Dict[Union[Type[RaiseExceptionRequestMiddleware], Type[CatchExceptionDoNotOverrideRequestMiddleware]], int], Dict[Type[ProcessResponseMiddleware], int], Dict[Type[AsyncDefPipeline], int], Dict[str, Tuple[int, int]], Type[FromCrawlerFileFeedStorage], Type[SimpleScheduler], Dict[str, Dict[str, Optional[Union[str, int]]]], Dict[Union[Type[FailProcessSpiderInputMiddleware], Type[LogExceptionMiddleware]], int], Dict[Type[DeferredPipeline], int], Dict[Union[Type[GeneratorFailMiddleware], Type[GeneratorDoNothingAfterFailureMiddleware], Type[GeneratorRecoverMiddleware], Type[GeneratorDoNothingAfterRecoveryMiddleware]], int], Dict[str, Union[str, List[str]]], List[int], Dict[str, Dict[Any, Any]], Dict[str, Dict[str, str]], Tuple[int], Type[LogOnStoreFileStorage], Type[FromCrawlerRFPDupeFilter], int, Dict[str, Union[str, Dict[str, bool]]], Dict[str, Union[str, List[str], List[Dict[str, int]]]], Dict[str, Dict[str, Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]]]]], Dict[Type[AlternativeCallbacksMiddleware], int], Dict[Type[DropSomeItemsPipeline], int], Dict[Type[InjectArgumentsSpiderMiddleware], int], Dict[str, Type[FTPFeedStorageWithoutFeedOptionsWithFromCrawler]], Type[FTPFeedStorageWithoutFeedOptionsWithFromCrawler], Dict[str, Union[str, List[Union[Type[FeedPostProcessedExportsTest.MyPlugin1], str]], bytes]], Type[DummyLazyDH], Dict[Type[AsyncDefNotAsyncioPipeline], int], Type[OffDH], Type[DummyDH], Dict[str, Optional[Union[str, List[str]]]], Dict[Type[AsyncDefAsyncioPipeline], int], SettingsAttribute, Dict[str, Optional[Union[str, int]]], Type[MinimalScheduler], Dict[str, Dict[str, Optional[str]]], Dict[str, Type[FileFeedStorageWithoutFeedOptions]], Type[S3FeedStorageWithoutFeedOptionsWithFromCrawler], Dict[str, Type[FromCrawlerCsvItemExporter]], Type[DirectDupeFilter], Dict[str, Dict[str, Union[int, str]]], Dict[str, Type[DummyLazyDH]], Dict[str, Type[FromCrawlerFileFeedStorage]], Dict[str, Union[int, str]], Type[FailingBlockingFeedStorage]]], priority: Union[int, str]='project') -> None:
        """
        Store a key/value attribute with a given priority.

        Settings should be populated *before* configuring the Crawler object
        (through the :meth:`~scrapy.crawler.Crawler.configure` method),
        otherwise they won't have any effect.

        :param name: the setting name
        :type name: str

        :param value: the value to associate with the setting
        :type value: object

        :param priority: the priority of the setting. Should be a key of
            :attr:`~scrapy.settings.SETTINGS_PRIORITIES` or an integer
        :type priority: str or int
        """
        self._assert_mutability()
        priority = get_settings_priority(priority)
        if name not in self:
            if isinstance(value, SettingsAttribute):
                self.attributes[name] = value
            else:
                self.attributes[name] = SettingsAttribute(value, priority)
        else:
            self.attributes[name].set(value, priority)

    def setdict(self, values: Union[Dict[str, Union[bool, List[str], List[List[str]]]], Dict[Any, Any], Dict[str, str], Dict[str, List[Any]], Dict[str, Dict[Union[Type[GeneratorFailMiddleware], Type[GeneratorDoNothingAfterFailureMiddleware], Type[GeneratorRecoverMiddleware], Type[GeneratorDoNothingAfterRecoveryMiddleware]], int]], Dict[str, Dict[Union[Type[FailProcessSpiderInputMiddleware], Type[LogExceptionMiddleware]], int]], Dict[str, Dict[Type[RecoveryMiddleware], int]], Dict[str, Dict[Union[Type[NotGeneratorFailMiddleware], Type[NotGeneratorDoNothingAfterFailureMiddleware], Type[NotGeneratorRecoverMiddleware], Type[NotGeneratorDoNothingAfterRecoveryMiddleware]], int]], Dict[str, Union[Dict[Type[InjectArgumentsDownloaderMiddleware], int], Dict[Type[InjectArgumentsSpiderMiddleware], int]]], Dict[str, Dict[str, int]], Dict[str, bool], Dict[str, Dict[Type[LogExceptionMiddleware], int]], Dict[str, Union[str, bool]]], priority: Union[int, str]='project') -> None:
        self.update(values, priority)

    def setmodule(self, module: Union[Dict[Any, Any], str], priority: Union[int, str]='project') -> None:
        """
        Store settings from a module with a given priority.

        This is a helper function that calls
        :meth:`~scrapy.settings.BaseSettings.set` for every globally declared
        uppercase variable of ``module`` with the provided ``priority``.

        :param module: the module or the path of the module
        :type module: types.ModuleType or str

        :param priority: the priority of the settings. Should be a key of
            :attr:`~scrapy.settings.SETTINGS_PRIORITIES` or an integer
        :type priority: str or int
        """
        self._assert_mutability()
        if isinstance(module, str):
            module = import_module(module)
        for key in dir(module):
            if key.isupper():
                self.set(key, getattr(module, key), priority)

    def update(self, values: Optional[Union[Dict[str, Type[OffDH]], Dict[str, Dict[str, Union[str, List[Union[Type[FeedPostProcessedExportsTest.MyPlugin1], str]], bytes]]], Dict[str, Type[FTPFeedStorageWithoutFeedOptions]], Dict[str, Union[Dict[str, Dict[str, str]], int]], Dict[str, Dict[str, Dict[str, Optional[str]]]], Dict[str, Dict[Type[AsyncDefPipeline], int]], Dict[str, Type[StdoutFeedStorageWithoutFeedOptions]], Dict[str, Union[str, Dict[str, Type[FileFeedStorageWithoutFeedOptions]]]], Dict[str, Union[str, Dict[str, Type[S3FeedStorageWithoutFeedOptions]]]], Dict[str, Type[FailingBlockingFeedStorage]], Dict[str, Dict[str, Union[str, List[str], int]]], Dict[str, List[Any]], Dict[str, str], Dict[Any, Any], Dict[str, Dict[Union[Type[NotGeneratorFailMiddleware], Type[NotGeneratorDoNothingAfterFailureMiddleware], Type[NotGeneratorRecoverMiddleware], Type[NotGeneratorDoNothingAfterRecoveryMiddleware]], int]], Dict[str, Union[str, Dict[str, Type[FTPFeedStorageWithoutFeedOptions]]]], Dict[str, Type[S3FeedStorageWithoutFeedOptions]], Dict[str, Union[Dict[str, Dict[str, str]], Dict[str, Type[FailingBlockingFeedStorage]]]], Dict[Union[Type[RaiseExceptionRequestMiddleware], Type[CatchExceptionOverrideRequestMiddleware]], int], Dict[str, Dict[str, None]], Dict[str, Dict[Type[AsyncDefAsyncioPipeline], int]], Dict[str, Type[DummyDH]], Dict[str, Union[str, Dict[str, Type[S3FeedStorageWithoutFeedOptionsWithFromCrawler]]]], Dict[str, Dict[Type[RecoveryMiddleware], int]], str, Dict[str, Dict[str, Dict[str, Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]], bytes]]]], Dict[str, Dict[str, Dict[str, Union[str, List[str], int]]]], Dict[str, Optional[Union[Dict[str, Dict[str, str]], str]]], Dict[str, Dict[str, Union[str, List[str], List[Dict[str, int]]]]], Dict[str, Optional[Union[bool, str]]], Dict[str, Tuple[int]], Dict[str, Union[str, Dict[str, Dict[str, str]]]], Dict[str, Union[List[Any], Dict[str, Dict[str, str]]]], Dict[str, Type[FileDownloadHandler]], Dict[str, Optional[Union[Dict[str, Dict[str, str]], bool]]], Dict[str, Dict[str, Union[str, Dict[str, bool]]]], Dict[str, Union[Dict[str, Dict[str, str]], Dict[str, Type[DummyBlockingFeedStorage]]]], Dict[str, None], Dict[str, Union[str, int, List[int]]], Dict[Type[SimplePipeline], int], Dict[str, Dict[Union[Type[GeneratorFailMiddleware], Type[GeneratorDoNothingAfterFailureMiddleware], Type[GeneratorRecoverMiddleware], Type[GeneratorDoNothingAfterRecoveryMiddleware]], int]], Dict[str, Union[Dict[str, Union[Dict[str, Union[str, List[str], int]], Dict[str, Optional[Union[str, List[str]]]]]], int]], Dict[str, Optional[int]], Dict[str, Union[Dict[Type[InjectArgumentsDownloaderMiddleware], int], Dict[Type[InjectArgumentsSpiderMiddleware], int]]], Dict[str, Dict[str, Type[DummyLazyDH]]], Dict[str, Dict[Type[SimplePipeline], int]], Dict[Union[Type[NotGeneratorFailMiddleware], Type[NotGeneratorDoNothingAfterFailureMiddleware], Type[NotGeneratorRecoverMiddleware], Type[NotGeneratorDoNothingAfterRecoveryMiddleware]], int], Dict[str, Union[str, List[str], int]], Dict[str, Type[S3FeedStorageWithoutFeedOptionsWithFromCrawler]], Dict[str, Dict[Union[Type[RaiseExceptionRequestMiddleware], Type[CatchExceptionDoNotOverrideRequestMiddleware]], int]], Dict[str, List[str]], Dict[str, Optional[str]], BaseSettings, Dict[Type[InjectArgumentsDownloaderMiddleware], int], Dict[str, Union[str, Dict[Type[DropSomeItemsPipeline], int]]], Dict[str, Dict[Union[Type[FailProcessSpiderInputMiddleware], Type[LogExceptionMiddleware]], int]], Dict[str, Dict[str, Dict[str, Union[str, List[str], List[Dict[str, int]]]]]], Dict[str, Dict[str, Union[Dict[str, Union[str, List[str], int]], Dict[str, Optional[Union[str, List[str]]]]]]], Dict[str, Dict[Union[Type[RaiseExceptionRequestMiddleware], Type[CatchExceptionOverrideRequestMiddleware]], int]], Dict[str, Union[str, Dict[Type[DropSomeItemsPipeline], int], Type[SkipMessagesLogFormatter]]], Dict[str, Type[SpiderLoaderWithWrongInterface]], Dict[str, Dict[str, Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]], bytes]]], Dict[Type[LogExceptionMiddleware], int], Dict[str, Type[LogOnStoreFileStorage]], Dict[str, Dict[str, Union[str, List[str]]]], Dict[str, float], Dict[str, Union[str, int, List[Any], List[str]]], Dict[str, bool], Dict[Type[RecoveryMiddleware], int], Dict[str, Union[str, Dict[str, Type[StdoutFeedStorageWithoutFeedOptions]]]], Dict[str, Union[List[str], Dict[str, Dict[str, str]]]], Dict[str, Union[int, BaseSettings]], Dict[str, Union[bool, Type[FromSettingsRFPDupeFilter]]], Dict[str, Dict[str, Type[OffDH]]], Dict[str, Union[Dict[str, Union[str, List[str], int]], Dict[str, Optional[Union[str, List[str]]]]]], Dict[str, Union[Dict[str, Type[FromCrawlerCsvItemExporter]], Dict[str, Type[FromCrawlerFileFeedStorage]], Dict[str, Dict[str, str]]]], Dict[str, Dict[str, int]], Dict[str, Dict[str, Type[DummyDH]]], Dict[Type[RaiseExceptionRequestMiddleware], int], Dict[str, int], Dict[str, Union[int, str, Dict[str, Tuple[int, int]]]], Dict[str, Union[Dict[str, Dict[str, str]], Dict[str, Type[LogOnStoreFileStorage]], bool]], Dict[str, Dict[str, Dict[str, Union[str, List[str]]]]], Dict[str, Type[DummyBlockingFeedStorage]], Dict[str, Dict[Type[RaiseExceptionRequestMiddleware], int]], Dict[str, Union[str, List[int], bool, BaseSettings]], Dict[Union[Type[RaiseExceptionRequestMiddleware], Type[CatchExceptionDoNotOverrideRequestMiddleware]], int], Dict[Type[ProcessResponseMiddleware], int], Dict[Type[AsyncDefPipeline], int], Dict[str, Dict[Type[ProcessResponseMiddleware], int]], Dict[str, Type[MinimalScheduler]], Dict[str, Dict[str, Optional[Union[str, int]]]], Dict[Union[Type[FailProcessSpiderInputMiddleware], Type[LogExceptionMiddleware]], int], Dict[str, Dict[str, Dict[str, Optional[Union[str, int]]]]], Dict[str, Dict[Type[AsyncDefNotAsyncioPipeline], int]], Dict[str, Dict[str, Dict[str, str]]], Dict[str, Dict[str, Dict[Any, Any]]], Dict[int, int], Dict[str, Type[SimpleScheduler]], Dict[str, Type[CustomPythonOrgPolicy]], Dict[Type[DeferredPipeline], int], Dict[Union[Type[GeneratorFailMiddleware], Type[GeneratorDoNothingAfterFailureMiddleware], Type[GeneratorRecoverMiddleware], Type[GeneratorDoNothingAfterRecoveryMiddleware]], int], Dict[str, Optional[Dict[str, Dict[str, str]]]], Dict[str, Union[Dict[str, int], str]], Dict[str, Dict[Any, Any]], Dict[str, Dict[str, str]], Dict[str, Dict[str, Dict[str, Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]]]]]], Dict[str, Union[List[str], bool]], Dict[str, Union[str, Dict[str, Type[FTPFeedStorageWithoutFeedOptionsWithFromCrawler]]]], Dict[str, Union[bool, List[str], List[List[str]]]], Dict[str, Dict[str, Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]]]]], Dict[Type[AlternativeCallbacksMiddleware], int], Dict[Type[DropSomeItemsPipeline], int], Dict[Type[InjectArgumentsSpiderMiddleware], int], Dict[str, Type[FTPFeedStorageWithoutFeedOptionsWithFromCrawler]], Dict[str, Union[bool, Type[FromCrawlerRFPDupeFilter]]], Dict[str, Union[float, bool]], Dict[str, Optional[Dict[str, Dict[str, Union[str, Dict[str, bool]]]]]], Dict[str, Dict[Type[DeferredPipeline], int]], Dict[Type[AsyncDefNotAsyncioPipeline], int], Dict[str, Optional[Union[Dict[str, Dict[str, str]], int]]], Dict[str, Dict[Type[AlternativeCallbacksMiddleware], int]], Dict[str, Union[Dict[str, int], str, bool]], Dict[str, BaseSettings], Dict[str, Dict[Type[LogExceptionMiddleware], int]], Dict[Type[AsyncDefAsyncioPipeline], int], Dict[str, Union[bool, Dict[str, Dict[str, str]]]], Dict[str, Union[str, int, List[Any]]], Dict[str, Dict[str, Optional[str]]], Dict[str, Type[FileFeedStorageWithoutFeedOptions]], Dict[str, Type[FromCrawlerCsvItemExporter]], Dict[str, Dict[str, Union[str, int]]], Dict[str, Union[bool, str]], Dict[str, Dict[str, Dict[str, Union[str, List[Union[Type[FeedPostProcessedExportsTest.MyPlugin1], str]], bytes]]]], Dict[str, Dict[str, Dict[str, Union[str, int]]]], Dict[str, Type[DummyLazyDH]], Dict[str, Union[str, List[str], int, Tuple[int, int, int, int]]], Dict[str, Type[FromCrawlerFileFeedStorage]], Dict[str, Union[str, int]], Dict[str, Type[DirectDupeFilter]]]], priority: Union[int, str]='project') -> None:
        """
        Store key/value pairs with a given priority.

        This is a helper function that calls
        :meth:`~scrapy.settings.BaseSettings.set` for every item of ``values``
        with the provided ``priority``.

        If ``values`` is a string, it is assumed to be JSON-encoded and parsed
        into a dict with ``json.loads()`` first. If it is a
        :class:`~scrapy.settings.BaseSettings` instance, the per-key priorities
        will be used and the ``priority`` parameter ignored. This allows
        inserting/updating settings with different priorities with a single
        command.

        :param values: the settings names and values
        :type values: dict or string or :class:`~scrapy.settings.BaseSettings`

        :param priority: the priority of the settings. Should be a key of
            :attr:`~scrapy.settings.SETTINGS_PRIORITIES` or an integer
        :type priority: str or int
        """
        self._assert_mutability()
        if isinstance(values, str):
            values = json.loads(values)
        if values is not None:
            if isinstance(values, BaseSettings):
                for name, value in values.items():
                    self.set(name, value, values.getpriority(name))
            else:
                for name, value in values.items():
                    self.set(name, value, priority)

    def delete(self, name: str, priority: str='project') -> None:
        self._assert_mutability()
        priority = get_settings_priority(priority)
        if priority >= self.getpriority(name):
            del self.attributes[name]

    def __delitem__(self, name: str) -> None:
        self._assert_mutability()
        del self.attributes[name]

    def _assert_mutability(self) -> None:
        if self.frozen:
            raise TypeError("Trying to modify an immutable Settings object")

    def copy(self) -> BaseSettings:
        """
        Make a deep copy of current settings.

        This method returns a new instance of the :class:`Settings` class,
        populated with the same values and their priorities.

        Modifications to the new object won't be reflected on the original
        settings.
        """
        return copy.deepcopy(self)

    def freeze(self) -> None:
        """
        Disable further changes to the current settings.

        After calling this method, the present state of the settings will become
        immutable. Trying to change values through the :meth:`~set` method and
        its variants won't be possible and will be alerted.
        """
        self.frozen = True

    def frozencopy(self) -> BaseSettings:
        """
        Return an immutable copy of the current settings.

        Alias for a :meth:`~freeze` call in the object returned by :meth:`copy`.
        """
        copy = self.copy()
        copy.freeze()
        return copy

    def __iter__(self):
        return iter(self.attributes)

    def __len__(self) -> int:
        return len(self.attributes)

    def _to_dict(self) -> Union[Dict[int, int], Dict[str, Union[str, List[int], bool, Dict[int, int]]]]:
        return {k: (v._to_dict() if isinstance(v, BaseSettings) else v)
                for k, v in self.items()}

    def copy_to_dict(self) -> Dict[str, Union[str, List[int], bool, Dict[int, int]]]:
        """
        Make a copy of current settings and convert to a dict.

        This method returns a new dict populated with the same values
        and their priorities as the current settings.

        Modifications to the returned dict won't be reflected on the original
        settings.

        This method can be useful for example for printing settings
        in Scrapy shell.
        """
        settings = self.copy()
        return settings._to_dict()

    def _repr_pretty_(self, p, cycle):
        if cycle:
            p.text(repr(self))
        else:
            p.text(pformat(self.copy_to_dict()))


class _DictProxy(MutableMapping):

    def __init__(self, settings, priority):
        self.o = {}
        self.settings = settings
        self.priority = priority

    def __len__(self):
        return len(self.o)

    def __getitem__(self, k):
        return self.o[k]

    def __setitem__(self, k, v):
        self.settings.set(k, v, priority=self.priority)
        self.o[k] = v

    def __delitem__(self, k):
        del self.o[k]

    def __iter__(self, k, v):
        return iter(self.o)


class Settings(BaseSettings):
    """
    This object stores Scrapy settings for the configuration of internal
    components, and can be used for any further customization.

    It is a direct subclass and supports all methods of
    :class:`~scrapy.settings.BaseSettings`. Additionally, after instantiation
    of this class, the new object will have the global default settings
    described on :ref:`topics-settings-ref` already populated.
    """

    def __init__(self, values: Optional[Union[Dict[str, Union[str, int, List[int]]], Dict[str, Union[Dict[str, Dict[str, str]], Dict[str, Type[LogOnStoreFileStorage]], bool]], Dict[str, Dict[str, Dict[str, Union[str, List[str]]]]], Dict[str, Union[bool, Type[FromCrawlerRFPDupeFilter]]], Dict[str, Union[float, bool]], Dict[str, Union[Dict[str, Dict[str, str]], int]], Dict[str, Dict[str, Type[DummyLazyDH]]], Dict[str, Dict[Type[RaiseExceptionRequestMiddleware], int]], Dict[str, Optional[Dict[str, Dict[str, Union[str, Dict[str, bool]]]]]], Dict[str, Dict[str, Dict[str, Optional[str]]]], Dict[str, Union[Dict[str, Union[Dict[str, Union[str, List[str], int]], Dict[str, Optional[Union[str, List[str]]]]]], int]], Dict[str, Dict[Type[DeferredPipeline], int]], Dict[str, Dict[Type[AsyncDefPipeline], int]], Dict[str, Optional[Union[Dict[str, Dict[str, str]], int]]], Dict[str, Dict[Type[SimplePipeline], int]], Dict[str, Union[str, List[str], int]], Dict[str, Union[str, Dict[str, Type[FileFeedStorageWithoutFeedOptions]]]], Dict[str, Dict[Type[ProcessResponseMiddleware], int]], Dict[str, Dict[Type[AlternativeCallbacksMiddleware], int]], Dict[str, Union[str, Dict[str, Type[S3FeedStorageWithoutFeedOptions]]]], Dict[str, Dict[Union[Type[RaiseExceptionRequestMiddleware], Type[CatchExceptionDoNotOverrideRequestMiddleware]], int]], Dict[str, List[str]], Dict[Any, Any], Dict[str, str], Dict[str, Optional[str]], Dict[str, Union[Dict[str, int], str, bool]], Dict[str, Type[MinimalScheduler]], Dict[str, Dict[str, Dict[str, Optional[Union[str, int]]]]], Dict[str, Union[str, Dict[Type[DropSomeItemsPipeline], int]]], Dict[str, Union[str, Dict[str, Type[FTPFeedStorageWithoutFeedOptions]]]], Dict[str, Dict[Type[AsyncDefNotAsyncioPipeline], int]], Dict[str, Dict[str, Dict[Any, Any]]], Dict[str, Dict[str, Dict[str, str]]], Dict[str, Union[Dict[str, Dict[str, str]], Dict[str, Type[FailingBlockingFeedStorage]]]], Dict[str, Type[SimpleScheduler]], Dict[str, Type[CustomPythonOrgPolicy]], Dict[str, Union[bool, Dict[str, Dict[str, str]]]], Dict[str, Dict[str, None]], Dict[str, Dict[Union[Type[RaiseExceptionRequestMiddleware], Type[CatchExceptionOverrideRequestMiddleware]], int]], Dict[str, Dict[str, Union[Dict[str, Union[str, List[str], int]], Dict[str, Optional[Union[str, List[str]]]]]]], Dict[str, Union[str, int, List[Any]]], Dict[str, Dict[Type[AsyncDefAsyncioPipeline], int]], Dict[str, Dict[str, Dict[str, Union[str, List[str], List[Dict[str, int]]]]]], Dict[str, Union[str, Dict[str, Type[S3FeedStorageWithoutFeedOptionsWithFromCrawler]]]], Dict[str, Type[SpiderLoaderWithWrongInterface]], Dict[str, Optional[Dict[str, Dict[str, str]]]], Dict[str, Union[str, Dict[Type[DropSomeItemsPipeline], int], Type[SkipMessagesLogFormatter]]], Dict[str, Union[Dict[str, int], str]], Settings, Dict[str, Dict[Any, Any]], Dict[str, int], Dict[str, Dict[str, str]], Dict[str, Dict[str, Dict[str, Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]], bytes]]]], Dict[str, float], Dict[str, Union[str, int, List[Any], List[str]]], Dict[str, bool], Dict[str, Dict[str, Dict[str, Union[str, List[str], int]]]], Dict[str, Dict[str, Dict[str, Union[str, List[Type[FeedPostProcessedExportsTest.MyPlugin1]]]]]], Dict[str, Union[bool, str]], Dict[str, Dict[str, Dict[str, Union[str, List[Union[Type[FeedPostProcessedExportsTest.MyPlugin1], str]], bytes]]]], Dict[str, Union[str, Dict[str, Type[FTPFeedStorageWithoutFeedOptionsWithFromCrawler]]]], Dict[str, Dict[str, Dict[str, Union[str, int]]]], Dict[str, Optional[Union[Dict[str, Dict[str, str]], str]]], Dict[str, Union[List[str], bool]], Dict[str, Optional[Union[bool, str]]], Dict[str, Tuple[int]], Dict[str, Union[str, Dict[str, Type[StdoutFeedStorageWithoutFeedOptions]]]], Dict[str, Union[List[Any], Dict[str, Dict[str, str]]]], Dict[str, Union[str, List[str], int, Tuple[int, int, int, int]]], Dict[str, Union[List[str], Dict[str, Dict[str, str]]]], Dict[str, Union[str, Dict[str, Dict[str, str]]]], Dict[str, Optional[Union[Dict[str, Dict[str, str]], bool]]], Dict[str, Union[str, int]], Dict[str, Union[bool, Type[FromSettingsRFPDupeFilter]]], Dict[str, Dict[str, Type[OffDH]]], Dict[str, Union[Dict[str, Dict[str, str]], Dict[str, Type[DummyBlockingFeedStorage]]]], Dict[str, None], Dict[str, Union[Dict[str, Type[FromCrawlerCsvItemExporter]], Dict[str, Type[FromCrawlerFileFeedStorage]], Dict[str, Dict[str, str]]]], Dict[str, Dict[str, int]], Dict[str, Dict[str, Type[DummyDH]]], Dict[str, Type[DirectDupeFilter]], Dict[str, Union[int, str, Dict[str, Tuple[int, int]]]]]]=None, priority: Union[int, str]='project') -> None:
        # Do not pass kwarg values here. We don't want to promote user-defined
        # dicts, and we want to update, not replace, default dicts with the
        # values given by the user
        super().__init__()
        self.setmodule(default_settings, 'default')
        # Promote default dictionaries to BaseSettings instances for per-key
        # priorities
        for name, val in self.items():
            if isinstance(val, dict):
                self.set(name, BaseSettings(val, 'default'), 'default')
        self.update(values, priority)


def iter_default_settings() -> Iterator[Union[Tuple[str, bool], Tuple[str, None], Tuple[str, float], Tuple[str, str], Tuple[str, int], Tuple[str, Dict[str, str]], Tuple[str, Dict[Any, Any]], Tuple[str, Dict[str, int]], Tuple[str, List[Any]], Tuple[str, List[str]], Tuple[str, List[int]]]]:
    """Return the default settings as an iterator of (name, value) tuples"""
    for name in dir(default_settings):
        if name.isupper():
            yield name, getattr(default_settings, name)


def overridden_settings(settings: Settings) -> Iterator[Union[Tuple[str, float], Tuple[str, Type[SimpleScheduler]], Tuple[str, int], Tuple[str, str], Tuple[str, bool], Tuple[str, List[str]], Tuple[str, List[Any]], Tuple[str, None], Tuple[str, Type[DirectDupeFilter]], Tuple[str, Type[MinimalScheduler]], Tuple[str, Type[SkipMessagesLogFormatter]], Tuple[str, Type[FromCrawlerRFPDupeFilter]], Tuple[str, Type[FromSettingsRFPDupeFilter]]]]:
    """Return a dict of the settings that have been overridden"""
    for name, defvalue in iter_default_settings():
        value = settings[name]
        if not isinstance(defvalue, dict) and value != defvalue:
            yield name, value
