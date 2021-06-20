from unittest import TestCase, skip
from unittest.mock import patch
import os
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
        self.assertEqual("{'status_code': 400, 'message': ''}", resp.__repr__())
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

    def test_method_send_request(self):
        """check response from Notix.send_notification"""
        response = Response()
        response.status_code = 200
        with patch.object(
                Notix,
                "_send_request",
                return_value=ResponseParser(response).parse(),
        ) as resp_ob:
            resp = Notix(**self.app_config)
            res = resp._send_request(url="fake_url")
            self.assertEqual(res["status_code"], resp_ob.return_value["status_code"])


class NotixRealScenarios(TestCase):
    """
    Testcases based on real app_id and token with 0 Subscribed users
    """
    def setUp(self) -> None:
        try:
            self.app_id = os.environ["APP_ID"]
            self.token = os.environ["TOKEN"]
            self.notix = Notix(app_id=self.app_id, token=self.token)
        except KeyError:
            self.skipTest("Envirnoment not set")

    def test_auth_check(self):
        resp = self.notix.check_auth()
        self.assertEqual(True, "success" in repr(resp).lower())
        self.assertEqual(200, resp["status_code"])

    def test_send_notification(self):
        """check response from Notix.send_notification"""
        data = {
            "title": "Sample title",
            "url": "https://docs.notix.co/example-icon.png",
            "icon": "https://docs.notix.co/example-icon.png",
            "text": "Hi there",
            "image": "https://docs.notix.co/example-icon.png",
        }
        resp = self.notix.send_notification(message=data)
        self.assertEqual(404, resp["status_code"])

    def test_remove_add_audience_with_pixel(self):
        """check response from Notix.remove_add_audience"""
        pixel = "fake_pixel_value"
        resp = self.notix.remove_add_audience_with_pixel(pixel=pixel)
        self.assertEqual(404, resp["status_code"])

    def test_add_audience(self):
        user = "test@test.com"
        resp = self.notix.add_audience(user=user, audience="test_audience")
        self.assertEqual(400, resp["status_code"])

    def test_remove_audience(self):
        user = "test@test.com"
        resp = self.notix.delete_audience(user=user, audience="test_audience")
        self.assertEqual(404, resp["status_code"])

    def test_sync_subscribed_users(self):
        user = "test@test.com"
        resp = self.notix.sync_subscribed_users(user=user)
        self.assertEqual(404, resp["status_code"])

    def test_send_method(self):
        url = "https://docs.notix.co/example-icon.png"
        method = "GET"
        resp = self.notix._send_request(
            url=url,
            method=method
        )
        self.assertEqual(404, resp["status_code"])