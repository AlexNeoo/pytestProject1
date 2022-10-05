import requests
from config import SERVICE_URL, SERVICE_URL_W
from helper_json import ValidateJson, ValidateJsonPydantic, ValidateBitcoin


def test_1():
    assert 1 == 1, "not equal !!!"
    print("Equal !!!")


def test_2():
    assert 1 != 0, "Equal !!!"
    print("Not Equal !!!")


def test_3():
    resp = requests.get(url=SERVICE_URL)

    ValidateJson(resp).check_status_code()
    ValidateJson(resp).check_len()
    ValidateJson(resp).check_schema()


def test_4():
    resp = requests.get(url=SERVICE_URL)

    ValidateJsonPydantic(resp).check_status_code()
    ValidateJsonPydantic(resp).check_len()
    ValidateJsonPydantic(resp).check_schema()


def test_5():
    resp = requests.get(url=SERVICE_URL_W)
    ValidateBitcoin(resp).check_status_code()
    print(resp.json())
    ValidateJsonPydantic(resp).check_len(dlina=4)
    # ValidateJsonPydantic(resp).check_schema()
