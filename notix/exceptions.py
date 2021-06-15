class BaseCustomException(Exception):
    """Base Exception"""


class UrlPathException(BaseCustomException):
    """Raises when url path doesnot exists"""
