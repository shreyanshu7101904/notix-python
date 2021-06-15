from notix.notix_api import get_url

def test_get_url():
    assert get_url("send") == "http://notix.io/api/send"
