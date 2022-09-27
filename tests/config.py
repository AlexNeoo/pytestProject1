from enum import Enum

SERVICE_URL = "https://my-json-server.typicode.com/typicode/demo/posts"


class ErrorMessage(Enum):
    WRONG_STATUS_CODE = "Actual code is Not equal to expected"
    WRONG_MESSAGE_LEN = "Actual message length is Not equal to expected"

