import requests as request_module
from os import environ
from .constants import URL_PATHS
from .exceptions import UrlPathException, EnvironmentNotSet

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
    """Response Parser class to Parse Notix Api Response"""

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

    def __init__(self, app_id: str = None, token: str = None):
        self._request = request_module
        if app_id and token:
            self._app_id = app_id
            self._token = token
        else:
            try:
                self._app_id = environ["APP_ID"]
                self._token = environ["TOKEN"]
            except KeyError:
                raise EnvironmentNotSet
        self._params = {"app": self._app_id}
        self._header = {"Authorization-Token": self._token}

    def _send_request(self, **kwargs) -> ResponseParser:
        """Send api request to notix client"""
        response = self._request.request(
            params=self._params, headers=self._header, **kwargs
        )
        return ResponseParser(response).parse()

    def check_auth(self):
        """
        Check authorisation Token using notix andbox
        :return: dict
        """
        return self._send_request(
            method="GET",
            url=get_url("check_auth"),
        )

    def send_notification(self, message: dict, limit: int = None, schedule: dict = None, target: dict = None) -> ResponseParser:
        """
        Notification sender method for notix class
        for full params visit here https://docs.notix.co/api-send.html
        :arg message : dict containing message details as described in api docs
        :arg limit : int pass int value for limiting message sent to subscribers
        :arg schedule : dict schedule object as described in notix api docs
        :arg target : dict containing audience targeting info as described in docs
        :return: dict
        """
        data = {
            "message": message,
            **({"limit": limit} if limit else {}),
            **({"schedule": schedule} if schedule else {}),
            **({"target": target} if target else {}),
        }
        return self._send_request(
            method="POST",
            url=get_url("send"),
            json=data,
        )

    def add_audience(self, audience, user) -> ResponseParser:
        """
        Add audience label to already subscribe users
        :param data: {"audience": "audience_identifier", "user":"user_identifier"}
        :return: ResponseParser
        """
        data = {
            "audience": audience,
            "user": user,
        }
        return self._send_request(method="POST", url=get_url("audience_add"), json=data)

    def delete_audience(self, audience, user) -> ResponseParser:
        """
        Delete audience label to already subscribe users
        :param data: {"audience": "audience_identifier", "user":"user_identifier"}
        :return: ResponseParser
        """
        data = {
            "audience": audience,
            "user": user,
        }
        return self._send_request(
            method="POST", url=get_url("delete_audience"), json=data
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
