from jsonschema import validate
from config import ErrorMessage, POST_SCHEMA, PydanticPost


class ValidateJson:
    def __init__(self, data):
        self.data = data

    def check_status_code(self):
        assert self.data.status_code == 200, \
            ErrorMessage.WRONG_STATUS_CODE.value

    def check_len(self):
        resp_data = self.data.json()
        assert len(resp_data) == 3, \
            ErrorMessage.WRONG_MESSAGE_LEN.value
        print(resp_data)

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
