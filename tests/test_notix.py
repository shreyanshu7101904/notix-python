from unittest import TestCase

from requests import Response

from notix.exceptions import UrlPathException
from notix.notix_api import ResponseParser, get_url


class GetUrlTest(TestCase):
    """
    `get_url` function test case class
    """

    def test_get_url(self):
        """ Test output from `get_url` function"""
        self.assertTrue("http://notix.io/api/send", get_url("send"))

    def test_get_url_exception(self):
        """ Test `UrlPathException` from `get_url` """
        self.assertRaises(UrlPathException, get_url, "test")


class ResponseParserTest(TestCase):
    """Response parser base class to test notifications"""

    response = Response()

    def test_bad_response_code(self):
        """test bad response code"""
        self.response.status_code = 400
        resp = ResponseParser(self.response).parse()
        self.assertTrue("400", resp["status_code"])

    def test_success_response_code(self):
        self.response.status_code = 200
        resp = ResponseParser(self.response).parse()
        self.assertTrue("200", resp["status_code"])
