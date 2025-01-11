import requests


class TestLength:
    def test_get_headers_positive(self):
        r = requests.post("https://playground.learnqa.ru/api/homework_header")
        print("\n", r.headers)
        assert r.headers, "Заголовки не были получены"

    def test_get_headers_negative(self):
        r = requests.post("https://wrong.endpoint")
        print("\n", r.headers)
        assert r.cookies, "Заголовки не были получены"