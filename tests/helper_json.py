from jsonschema import validate
from config import ErrorMessage, POST_SCHEMA, PydanticPost, BitcoinPost


class ValidateJson:
    def __init__(self, data):
        self.data = data

    def check_status_code(self):
        assert self.data.status_code == 200, \
            ErrorMessage.WRONG_STATUS_CODE.value

    def check_len(self, dlina=3):
        resp_data = self.data.json()
        print(len(resp_data))
        assert len(resp_data) == dlina, \
            ErrorMessage.WRONG_MESSAGE_LEN.value

    def check_schema(self):
        resp_data = self.data.json()
        for item in resp_data:
            validate(item, POST_SCHEMA)
        print(resp_data)


class ValidateJsonPydantic(ValidateJson):
    def __init__(self, data):
        super().__init__(data)

    def check_schema(self):
        resp_data = self.data.json()
        for item in resp_data:
            PydanticPost.parse_obj(item)
        print(resp_data)


class ValidateBitcoin(ValidateJson):
    def __init__(self, data):
        super().__init__(data)

    def check_schema(self):
        resp_data = self.data.json()
        for item in resp_data:
            BitcoinPost.parse_obj(item)
        print(resp_data)
