from enum import Enum
from pydantic import BaseModel, validator, Field


SERVICE_URL = "https://my-json-server.typicode.com/typicode/demo/posts"

SERVICE_URL_W = "https://api.coindesk.com/v1/bpi/currentprice.json"

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

class BitcoinPost(BaseModel):
    disclaimer: str
    chartName: str
    # nane: str = Field(alias="_nane")

    @validator("chartName")
    def check_chartName(cls, value):
        if value != "Bitcoin":
            raise ValueError(ErrorMessage.WRONG_ID_LEN.value)
        else:
            return value

#
# {
#     "time": {
#         "updated": "Oct 5, 2022 22:05:00 UTC",
#         "updatedISO": "2022-10-05T22:05:00+00:00",
#         "updateduk": "Oct 5, 2022 at 23:05 BST\n"
#     },
#     "disclaimer": "This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from o\npenexchangerates.org",
#     "chartName": "Bitcoin",
#     "bpi": {
#         "USD": {
#             "code": "USD",
#             "symbol": "&#36;",
#             "rate": "20,053.4841",
#             "description": "United States Doll\nar",
#             "rate_float": 20053.4841
#         },
#         "GBP": {
#             "code": "GBP",
#             "symbol": "&pound;",
#             "rate": "16,756.5309",
#             "description": "British Pound Sterling",
#             "rate_float": 16756.5309
#         },
#         "EUR": {
#             "code": "EUR",
#             "symbol": "&euro;",
#             "rate": "19,535.0213",
#             "description": "Euro",
#             "rate_float": 19535.0213
#         }
#     }
# }

class ErrorMessage(Enum):
    WRONG_STATUS_CODE = "Actual code is Not equal to expected"
    WRONG_MESSAGE_LEN = "Actual message length is Not equal to expected"
    WRONG_FIELD_VAL = "Actual Field value is Not equal to expected"
    WRONG_ID_LEN = "Wrong Id value"
