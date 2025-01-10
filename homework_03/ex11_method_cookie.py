import requests


class TestLength:
    def test_get_cookie(self):
        r = requests.post("https://playground.learnqa.ru/api/homework_cookie")
        # print(r.cookies.get())
        print(r.status_code)
        print(r.text)
