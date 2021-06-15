from constants import URL_PATHS
from exceptions import UrlPathException


def get_url(path_name: str) -> str:
    """
    Url builder function to create `Notix` Api url based on parameter
    :param path_name: `Notix` url path string
    :return: url
    """
    try:
        return "http://notix.io/api" + URL_PATHS[path_name]
    except KeyError:
        raise UrlPathException
