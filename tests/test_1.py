import requests
from config import SERVICE_URL


def test_1():
    assert 1 == 1, "not equal !!!"
    print("Equal !!!")


def test_2():
    assert 1 != 0, "Equal !!!"
    print("Not Equal !!!")


def test_get():
    resp = requests.get(url=SERVICE_URL)
