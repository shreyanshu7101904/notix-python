class BaseCustomException(Exception):
    """Base Exception"""


class UrlPathException(BaseCustomException):
    """Raises when url path does not exists"""
    def __init__(self):
        super().__init__("Url Path parameter does not exists. Kindly provide valid url path")


class EnvironmentNotSet(BaseCustomException):
    """APP_ID and TOKEN Environment variables are not set"""

    def __init__(self):
        super().__init__("APP_ID and TOKEN Environment variables are not set")