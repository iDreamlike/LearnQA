import requests


response = requests.get("https://playground.learnqa.ru/api/long_redirect")
count_of_urls = len(response.history)

for i in range(0, count_of_urls):
    print(response.history[i].url)

print(f"Количество редиректов: {count_of_urls - 1}\nПоследний url: {response.history[count_of_urls-1].url}")
