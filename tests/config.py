from enum import Enum


class ErrorMessage(Enum):
    WRONG_STATUS_CODE = "Actual code is Not equal to expected"


SERVICE_URL = "https://my-json-server.typicode.com/typicode/demo/posts"
