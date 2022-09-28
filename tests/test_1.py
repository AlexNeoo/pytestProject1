import requests
from config import SERVICE_URL
from helper_json import ValidateJson


def test_1():
    assert 1 == 1, "not equal !!!"
    print("Equal !!!")


def test_2():
    assert 1 != 0, "Equal !!!"
    print("Not Equal !!!")


def test_get():
    resp = requests.get(url=SERVICE_URL)

    ValidateJson(resp).check_status_code()
    ValidateJson(resp).check_len()
    ValidateJson(resp).check_schema()
