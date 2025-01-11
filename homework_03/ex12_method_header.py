import requests


class TestHeaders:
    def test_get_headers_positive(self):
        r = requests.post("https://playground.learnqa.ru/api/homework_header")
        print("\n", r.headers)
        assert r.headers, "Заголовки не были получены"

    def test_get_headers_negative(self):
        r = requests.post("https://playground.learnqa.ru/api/homework_header")
        r.headers = None
        assert r.headers, "Заголовки не были получены"