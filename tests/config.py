from enum import Enum
from pydantic import BaseModel, validator, Field


SERVICE_URL = "https://my-json-server.typicode.com/typicode/demo/posts"

SERVICE_URL_W = "https://api2.binance.com/api/v3/ticker/24hr"

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
    symbol: str
    priceChange: float
    count: int
    # nane: str = Field(alias="_nane")
    #
    # @validator("chartName")
    # def check_chartName(cls, value):
    #     if value != "Bitcoin":
    #         raise ValueError(ErrorMessage.WRONG_FIELD_VAL.value)
    #     else:
    #         return value

# [
#   {
#     "symbol": "ETHBTC",
#     "priceChange": "0.00029200",
#     "priceChangePercent": "0.436",
#     "weightedAvgPrice": "0.06689296",
#     "prevClosePrice": "0.06693000",
#     "lastPrice": "0.06722300",
#     "lastQty": "0.95220000",
#     "bidPrice": "0.06722300",
#     "bidQty": "21.97560000",
#     "askPrice": "0.06722400",
#     "askQty": "30.34010000",
#     "openPrice": "0.06693100",
#     "highPrice": "0.06738500",
#     "lowPrice": "0.06635000",
#     "volume": "101014.11040000",
#     "quoteVolume": "6757.13236649",
#     "openTime": 1664923432391,
#     "closeTime": 1665009832391,
#     "firstId": 379842112,
#     "lastId": 380073581,
#     "count": 231470
#   },
#   {
#     "symbol": "LTCBTC",
#     "priceChange": "-0.00002600",
#     "priceChangePercent": "-0.953",
#     "weightedAvgPrice": "0.00270518",
#     "prevClosePrice": "0.00272700",
#     "lastPrice": "0.00270100",
#     "lastQty": "0.64000000",
#     "bidPrice": "0.00270100",
#     "bidQty": "28.50000000",
#     "askPrice": "0.00270200",
#     "askQty": "35.99800000",
#     "openPrice": "0.00272700",
#     "highPrice": "0.00273100",
#     "lowPrice": "0.00268100",
#     "volume": "56643.03200000",
#     "quoteVolume": "153.22942816",
#     "openTime": 1664923430489,
#     "closeTime": 1665009830489,
#     "firstId": 84103229,
#     "lastId": 84120619,
#     "count": 17391
#   },


class ErrorMessage(Enum):
    WRONG_STATUS_CODE = "Actual code is Not equal to expected"
    WRONG_MESSAGE_LEN = "Actual message length is Not equal to expected"
    WRONG_FIELD_VAL = "Actual Field value is Not equal to expected"
    WRONG_ID_LEN = "Wrong Id value"
