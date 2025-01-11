import json
import requests
import pytest


class TestUserAgent:
    data_provider = [
        [{"user-agent": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30", "platform":"Mobile","browser":"No","device":"Android"}, {"platform":"Mobile","browser":"No","device":"Android"}],
        [{"user-agent": "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"}, {"platform":"Mobile","browser":"Chrome","device":"iOS"}],
        [{"user-agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}, {"platform":"Googlebot","browser":"Unknown","device":"Unknown"}],
        [{"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"}, {"platform":"Web","browser":"Chrome","device":"No"}],
        [{"user-agent": "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}, {"platform":"Mobile","browser":"No","device":"iPhone"}]
    ]

    @pytest.mark.parametrize("data_provider", data_provider)
    def test_user_agent(self, data_provider):

        r = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers=data_provider[0])
        print("\n", r.text)

        fact_data = json.loads(r.text)

        assert fact_data['platform'] == data_provider[1]['platform'], f"Платформа не совпадает. Проблема при запросе с UserAgent: {data_provider[0]['user-agent']}"
        assert fact_data['browser'] == data_provider[1]['browser'], f"Браузер не совпадает. Проблема при запросе с UserAgent: {data_provider[0]['user-agent']}"
        assert fact_data['device'] == data_provider[1]['device'], f"Устройство не совпадает. Проблема при запросе с UserAgent: {data_provider[0]['user-agent']}"