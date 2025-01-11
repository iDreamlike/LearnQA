import requests


class TestLength:
    def test_get_cookie_positive(self):
        r = requests.post("https://playground.learnqa.ru/api/homework_cookie")
        print(dict(r.cookies))
        assert r.cookies, "Куки не были получены"

    def test_get_cookie_negative(self):
        r = requests.post("https://wrong.endpoint")
        print(dict(r.cookies))
        assert r.cookies, "Куки не были получены"