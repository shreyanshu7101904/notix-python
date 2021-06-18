from unittest import TestCase
from unittest.mock import MagicMock, patch

from requests import Response

from notix.exceptions import UrlPathException
from notix.notix_api import Notix, ResponseParser, get_url


class GetUrlTest(TestCase):
    """
    `get_url` function test case class
    """

    def test_get_url(self):
        """Test output from `get_url` function"""
        self.assertTrue("http://notix.io/api/send", get_url("send"))

    def test_get_url_exception(self):
        """Test `UrlPathException` from `get_url`"""
        self.assertRaises(UrlPathException, get_url, "test")


class ResponseParserTest(TestCase):
    """Response parser base class to test notifications"""

    response = Response()

    def test_bad_response_code(self):
        """test bad response code"""
        self.response.status_code = 400
        resp = ResponseParser(self.response).parse()
        self.assertEqual("{'status_code': 400, 'message': ''}", str(resp))
        self.assertTrue("400", resp["status_code"])

    def test_success_response_code(self):
        self.response.status_code = 200
        resp = ResponseParser(self.response).parse()
        self.assertTrue("200", resp["status_code"])


class NotixApiTest(TestCase):
    """Notix Class Test Cases"""

    app_config = {"app_id": "fake_app_id", "token": "fake_app_token"}

    def test_check_auth(self):
        """check response from Notix.check_auth i"""
        response = Response()
        response.status_code = 200
        with patch.object(
            Notix, "check_auth", return_value=ResponseParser(response).parse()
        ) as auth_method:
            auth = Notix(**self.app_config)
            auth.check_auth()
            self.assertEqual(200, auth_method.return_value["status_code"])
        with patch.object(
            Notix, "check_auth", return_value=ResponseParser(response).parse()
        ) as auth_method:
            auth = Notix(**self.app_config)
            auth.check_auth()
            self.assertNotEqual(500, auth_method.return_value["status_code"])

    def test_send_request(self):
        """check response from Notix._send_requests"""
        response = Response()
        response.status_code = 200
        params = {"url": "fake_url", "method": "GET", "json": {}}
        with patch.object(
            Notix, "_send_request", return_value=ResponseParser(response).parse()
        ) as send_request:
            send_request_ = Notix(**self.app_config)
            send_request_._send_request(**params)
            self.assertEqual(200, send_request.return_value["status_code"])

    def test_send_notification(self):
        """check response from Notix.send_notification"""
        response = Response()
        response.status_code = 200
        data = {"message": {"title": "Sample title", "url": "Sample url"}}
        with patch.object(
            Notix, "send_notification", return_value=ResponseParser(response).parse()
        ) as send_notification_method:
            send_notification = Notix(**self.app_config)
            send_notification.send_notification(data=data)
            self.assertEqual(200, send_notification_method.return_value["status_code"])

        with patch.object(
            Notix, "send_notification", return_value=ResponseParser(response).parse()
        ) as send_notification_method:
            send_notification = Notix(**self.app_config)
            send_notification.send_notification(data=data)
            self.assertNotEqual(
                500, send_notification_method.return_value["status_code"]
            )

    def test_remove_add_audience_with_pixel(self):
        """check response from Notix.send_notification"""
        response = Response()
        response.status_code = 200
        pixel = "fake_pixel_value"
        with patch.object(
            Notix,
            "remove_add_audience_with_pixel",
            return_value=ResponseParser(response).parse(),
        ) as audience:
            pixel_audience = Notix(**self.app_config)
            pixel_audience.remove_add_audience_with_pixel(pixel=pixel)
            self.assertEqual(200, audience.return_value["status_code"])
