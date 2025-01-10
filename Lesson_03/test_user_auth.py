import pytest
import requests


class TestUserAuth:
    exclude_params = [
        ("no_cookies"),
        ("no_token")
    ]

    def setup_method(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        assert "auth_sid" in response1.cookies, "Нет авторизационных куки в ответе"
        assert "x-csrf-token" in response1.headers, "Нет CSRF token header в ответе"
        assert "user_id" in response1.json(), "Нет user id в ответе"

        self.auth_sid = response1.cookies.get("auth_sid")
        self.token = response1.headers.get("x-csrf-token")
        self.user_id_from_auth_method = response1.json()["user_id"]


    def test_auth_user(self):
        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        assert "user_id" in response2.json(), "Нет user id во втором запросе"
        user_id_from_check_method = response2.json()["user_id"]

        assert self.user_id_from_auth_method == user_id_from_check_method, "User id из метода авторизации не соответствует user id из метода проверки"




    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):
        if condition == "no_cookies":
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers = {"x-csrf-token": self.token}
            )
        else:
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers={"auth_sid": self.auth_sid}
            )

        assert "user_id" in response2.json(), "Нет user id во втором запросе"

        user_id_from_check_method = response2.json()["user_id"]

        assert user_id_from_check_method == 0, f"User is authorized with condition {condition}"
