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

    def __str__(self):
        return f"Status Code = {self._response.status_code}, message = {self._response.text}"

    def parse(self):
        return {
            "status_code": self._response.status_code,
            "message": self._response.text
        }


class Notix(BaseNotix):
    """
    Notix class
    """

    def __init__(self, app_id, token):
        self._app_id = app_id
        self._request = request_module
        self._params = {
            "app_id": self._app_id
        }
        self._header = {
            "Authorization-Token": token
        }

    def send_notification(self, data) -> dict:
        """
        Notification sender method for notix class
        :param data: dict as mentioned in notix docs https://docs.notix.co/api-send.html as request body
        :return: dict
        """
        response = self._request.request(
            method="POST",
            url=get_url("send"),
            params=self._params,
            headers=self._header,
            json=data
        )
        return ResponseParser(response).parse()

