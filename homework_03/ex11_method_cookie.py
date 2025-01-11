import requests


class TestCookie:
    def test_get_cookie_positive(self):
        r = requests.post("https://playground.learnqa.ru/api/homework_cookie")
        print("\n", dict(r.cookies))
        assert r.cookies, "Куки не были получены"

    def test_get_cookie_negative(self):
        r = requests.post("https://playground.learnqa.ru/api/homework_cookie")
        r.cookies = None
        assert r.cookies, "Куки не были получены"