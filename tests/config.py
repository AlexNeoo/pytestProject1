from enum import Enum
from pydentic import *


SERVICE_URL = "https://my-json-server.typicode.com/typicode/demo/posts"

POST_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "title": {"title": "string",
                  #"enum": ["Post*"]
                  },
    },
    "required": ["id"]
}


class PydPost(BaseModel):
    pass


class ErrorMessage(Enum):
    WRONG_STATUS_CODE = "Actual code is Not equal to expected"
    WRONG_MESSAGE_LEN = "Actual message length is Not equal to expected"

