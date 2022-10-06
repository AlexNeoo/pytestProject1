import pytest


@pytest.fixture(autouse=True)
def start():
    print("Starting test")