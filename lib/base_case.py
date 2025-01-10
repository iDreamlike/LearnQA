import json.decoder

from requests import Response


class BaseCase:
    def get_cookie (self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Не можем найти cookie с именем {cookie_name} в последнем ответе"
        return response.cookies[cookie_name]

    def get_header (self, response: Response, headers_name):
        assert headers_name in response.headers, f"Не можем найти header с именем {headers_name} в последнем ответе"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Ответ не в JSON формате. Текст ответа: '{response.text}'"

        assert name in response_as_dict, f"Ответ JSON не имеет ключа '{name}'"

        return response_as_dict[name]
