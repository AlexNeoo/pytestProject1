from enum import Enum
from pydantic import BaseModel, validator, Field


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


class PydanticPost(BaseModel):
    id: int
    title: str
    # nane: str = Field(alias="_nane")

    @validator("id")
    def check_id(cls, value):
        if value >= 4:
            raise ValueError(ErrorMessage.WRONG_ID_LEN.value)
        else:
            return value


class ErrorMessage(Enum):
    WRONG_STATUS_CODE = "Actual code is Not equal to expected"
    WRONG_MESSAGE_LEN = "Actual message length is Not equal to expected"
    WRONG_ID_LEN = "Wrong Id value"
