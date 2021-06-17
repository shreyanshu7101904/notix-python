import requests as request_module

from .constants import URL_PATHS
from .exceptions import UrlPathException

NOTIX_URL = "http://notix.io/api"


# Notix base Url


def get_url(path_name: str) -> str:
    """
    Url builder function to create `Notix` Api url based on parameter
    :param path_name: `Notix` url path string
    :return: url
    :raises UrlPathException
    """
    try:
        return NOTIX_URL + URL_PATHS[path_name]
    except KeyError:
        raise UrlPathException


class BaseNotix:
    """Base Notix Wrapper class"""


class BaseResponseParser:
    """Base Response parser class for all api calls"""


class ResponseParser(BaseResponseParser):
    def __init__(self, response):
        self._response = response

    def __repr__(self):
        return f"Status Code = {self._response.status_code}, message = {self._response.text}"

    def parse(self):
        return {
            "status_code": self._response.status_code,
            "message": self._response.text,
        }


class Notix(BaseNotix):
    """
    Notix class
    """

    def __init__(self, app_id, token):
        self._app_id = app_id
        self._request = request_module
        self._params = {"app_id": self._app_id}
        self._header = {"Authorization-Token": token}

    def _send_request(self, **kwargs) -> ResponseParser:
        """Send api request to notix client"""
        response = self._request.request(
            params=self._params,
            headers=self._header,
            **kwargs
        )
        return ResponseParser(response).parse()

    def check_auth(self):
        """
        Check authorisation Token using notix andbox
        :return: dict
        """
        return self._send_request()

    def send_notification(self, data) -> ResponseParser:
        """
        Notification sender method for notix class
        :arg data: dict as mentioned in notix docs
         https://docs.notix.co/api-send.html as request body
        :return: dict
        sample_data = {
            "limit": int,
            "message": {
                "icon": str,
                "image": "str",
                "text": "str",
                "title": "str",
                "url": str,
            },
            "schedule": {},
            "target": {}
        }
        """
        return self._send_request(
            method="POST",
            url=get_url("send"),
            json=data,
        )

    def add_audience(self, data: dict) -> ResponseParser:
        """
        Add audience label to already subscribe users
        :param data: {"audience": "audience_identifier", "user":"user_identifier"}
        :return: ResponseParser
        """
        return self._send_request(
            method="POST",
            url=get_url("audience_add"),
            json=data
        )

    def delete_audience(self, data: dict) -> ResponseParser:
        """
        Delete audience label to already subscribe users
        :param data: {"audience": "audience_identifier", "user":"user_identifier"}
        :return: ResponseParser
        """
        return self._send_request(
            method="POST",
            url=get_url("delete_audience"),
            json=data
        )

    def sync_subscribed_users(self, user: str):
        """
        Synchronize already subscribed users, Cookie Sync Pixel
        :param user: User Identifier as described by publisher
        :return: ResponseParser
        """
        self._params["user"] = user
        return self._send_request(
            method="GET",
            url=get_url("sync_user"),
        )

    def remove_add_audience_with_pixel(self, pixel: str) -> ResponseParser:
        """
        Delete audience label to already subscribe users
        :param pixel: Unique Pixel Identifier
        :return: ResponseParser
        """
        self._params["px"] = pixel
        return self._send_request(
            method="GET",
            url=get_url("retargeting"),
        )
