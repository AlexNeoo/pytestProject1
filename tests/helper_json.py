import requests
from jsonschema import validate
from config import SERVICE_URL, ErrorMessage, POST_SCHEMA


def test_get():
    resp = requests.get(url=SERVICE_URL)
    assert resp.status_code == 200, \
        ErrorMessage.WRONG_STATUS_CODE.value

    resp_data = resp.json()
    assert len(resp_data) == 3, \
        ErrorMessage.WRONG_MESSAGE_LEN.value

    for item in resp_data:
        validate(item, POST_SCHEMA)

    print(resp_data)