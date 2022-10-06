import pytest


@pytest.fixture(autouse=False, scope="session")
def start():
    print("Starting test")
    return 300
