import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegister(BaseCase):
    base_case = BaseCase()
    data_without_required_fields = [
            {'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': base_case.prepare_registration_email()},
            {'password': '123', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': base_case.prepare_registration_email()},
            {'password': '123', 'username': 'learnqa', 'lastName': 'learnqa', 'email': base_case.prepare_registration_email()},
            {'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'email': base_case.prepare_registration_email()},
            {'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa'}
        ]
    valid_email = base_case.prepare_registration_email()
    data_with_short_name = {
        'password': '123',
        'username': 'l',
        'firstName': 'learnqa',
        'lastName': 'learnqa',
        'email': valid_email}


    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")


    def test_create_user_with_existing_email(self):
        email='vinkotov@example.com'
        data = self.prepare_registration_data(email)
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"


    def test_create_user_with_wrong_email(self):
        email='testNameExample.com'
        data = self.prepare_registration_data(email)
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_code_status(response, 400)


    @pytest.mark.parametrize('data', data_without_required_fields)
    def test_create_user_without_required_fields(self, data):
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        print(data)
        Assertions.assert_code_status(response, 400)


    def test_create_user_with_short_name(self):
        valid_email = self.prepare_registration_email()
        data_with_short_name = {
            'password': '123',
            'username': 'l',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': valid_email}
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data_with_short_name)
        Assertions.assert_code_status(response, 400)


    def test_create_user_with_long_name(self):
        valid_email = self.prepare_registration_email()
        data_with_long_name = {
            'password': '123',
            'username': """11111111111111111111111111111111111111111111111111
            11111111111111111111111111111111111111111111111111
            11111111111111111111111111111111111111111111111111
            11111111111111111111111111111111111111111111111111
            11111111111111111111111111111111111111111111111111""",
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': valid_email}
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data_with_long_name)
        Assertions.assert_code_status(response, 400)