"""
This module contains some assorted functions used in tests
"""

import asyncio
import os
from posixpath import split
from unittest import mock

from importlib import import_module
from twisted.trial.unittest import SkipTest

from scrapy.utils.boto import is_botocore_available
from scrapy.http.response import Response
from tests.test_downloadermiddleware_decompression import DecompressionMiddlewareTest
from typing import Any, Dict, Iterator, List, Optional, Tuple, Type, Union
from unittest.mock import MagicMock


def assert_gcs_environ():
    if 'GCS_PROJECT_ID' not in os.environ:
        raise SkipTest("GCS_PROJECT_ID not found")


def skip_if_no_boto() -> None:
    if not is_botocore_available():
        raise SkipTest('missing botocore library')


def get_gcs_content_and_delete(bucket, path):
    from google.cloud import storage
    client = storage.Client(project=os.environ.get('GCS_PROJECT_ID'))
    bucket = client.get_bucket(bucket)
    blob = bucket.get_blob(path)
    content = blob.download_as_string()
    acl = list(blob.acl)  # loads acl before it will be deleted
    bucket.delete_blob(path)
    return content, acl, blob


def get_ftp_content_and_delete(
        path, host, port, username,
        password, use_active_mode=False):
    from ftplib import FTP
    ftp = FTP()
    ftp.connect(host, port)
    ftp.login(username, password)
    if use_active_mode:
        ftp.set_pasv(False)
    ftp_data = []

    def buffer_data(data):
        ftp_data.append(data)
    ftp.retrbinary(f'RETR {path}', buffer_data)
    dirname, filename = split(path)
    ftp.cwd(dirname)
    ftp.delete(filename)
    return "".join(ftp_data)


def get_crawler(spidercls: Optional[Union[Type[NotGeneratorCallbackSpiderMiddlewareRightAfterSpider], Type[ErrorSpider], Type[AttrsItemsSpider], Type[NotGeneratorCallbackSpider], Type[ItemSpider], Type[TestSpider], Type[SignalCatcherSpider], Type[DictItemsSpider], Type[GeneratorCallbackSpiderMiddlewareRightAfterSpider], Type[NotGeneratorOutputChainSpider], Type[SimpleSpider], Type[TestDupeFilterSpider], Type[_HttpErrorSpider], Type[ProcessSpiderInputSpiderWithErrback], Type[ItemSpider], Type[GeneratorCallbackSpider], Type[Spider], Type[FollowAllSpider], Type[RecoverySpider], Type[ItemSpider], Type[ProcessSpiderInputSpiderWithoutErrback], Type[StartUrlsSpider], Type[ItemZeroDivisionErrorSpider], Type[GeneratorOutputChainSpider], Type[ChangeCloseReasonSpider], Type[SingleRequestSpider], Type[DataClassItemsSpider]]]=None, settings_dict: Optional[Union[Dict[str, Union[str, Dict[str, Dict[str, str]]]], Dict[str, Union[str, Dict[str, Type[S3FeedStorageWithoutFeedOptionsWithFromCrawler]]]], Dict[str, Union[str, Dict[str, Type[FileFeedStorageWithoutFeedOptions]]]], Dict[str, Dict[str, Type[DummyLazyDH]]], Dict[str, Union[str, Dict[str, Type[StdoutFeedStorageWithoutFeedOptions]]]], Dict[str, Union[str, Dict[str, Type[FTPFeedStorageWithoutFeedOptions]]]], Dict[str, List[str]], Dict[Any, Any], Dict[str, str], Dict[str, Dict[Type[AsyncDefAsyncioPipeline], int]], Dict[str, Dict[Type[AsyncDefPipeline], int]], Dict[str, Union[str, Dict[str, Type[FTPFeedStorageWithoutFeedOptionsWithFromCrawler]]]], Dict[str, Dict[Type[SimplePipeline], int]], Dict[str, Dict[str, Dict[str, str]]], Dict[str, Dict[str, Dict[Any, Any]]], Dict[str, Dict[str, None]], Dict[str, Union[bool, Type[FromSettingsRFPDupeFilter]]], Dict[str, Optional[str]], Dict[str, Union[Dict[str, Dict[str, str]], int]], Dict[str, Dict[str, Type[OffDH]]], Dict[str, Dict[Type[DeferredPipeline], int]], Dict[str, Dict[Type[AsyncDefNotAsyncioPipeline], int]], Dict[str, Dict[Any, Any]], Dict[str, Dict[str, str]], Dict[str, float], Dict[str, bool], Dict[str, Dict[str, Type[DummyDH]]], Dict[str, Union[str, Dict[str, Type[S3FeedStorageWithoutFeedOptions]]]], Dict[str, Type[DirectDupeFilter]], Dict[str, None], Dict[str, Union[bool, Type[FromCrawlerRFPDupeFilter]]], Dict[str, int]]]=None) -> Crawler:
    """Return an unconfigured Crawler object. If settings_dict is given, it
    will be used to populate the crawler settings with a project level
    priority.
    """
    from scrapy.crawler import Crawler, CrawlerRunner
    from scrapy.spiders import Spider

    runner = CrawlerRunner(settings_dict)
    return runner.create_crawler(spidercls or Spider)


def get_pythonpath() -> str:
    """Return a PYTHONPATH suitable to use in processes so that they find this
    installation of Scrapy"""
    scrapy_path = import_module('scrapy').__path__[0]
    return os.path.dirname(scrapy_path) + os.pathsep + os.environ.get('PYTHONPATH', '')


def get_testenv() -> Dict[str, str]:
    """Return a OS environment dict suitable to fork processes that need to import
    this installation of Scrapy, instead of a system installed one.
    """
    env = os.environ.copy()
    env['PYTHONPATH'] = get_pythonpath()
    return env


def assert_samelines(testcase: DecompressionMiddlewareTest, text1: bytes, text2: bytes, msg: Optional[str]=None) -> None:
    """Asserts text1 and text2 have the same lines, ignoring differences in
    line endings between platforms
    """
    testcase.assertEqual(text1.splitlines(), text2.splitlines(), msg)


def get_from_asyncio_queue(value: Union[Response, int, str, Dict[str, int]]) -> Iterator[Any]:
    q = asyncio.Queue()
    getter = q.get()
    q.put_nowait(value)
    return getter


def mock_google_cloud_storage() -> Tuple[MagicMock, MagicMock, MagicMock]:
    """Creates autospec mocks for google-cloud-storage Client, Bucket and Blob
    classes and set their proper return values.
    """
    from google.cloud.storage import Client, Bucket, Blob
    client_mock = mock.create_autospec(Client)

    bucket_mock = mock.create_autospec(Bucket)
    client_mock.get_bucket.return_value = bucket_mock

    blob_mock = mock.create_autospec(Blob)
    bucket_mock.blob.return_value = blob_mock

    return (client_mock, bucket_mock, blob_mock)
