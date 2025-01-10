import requests


# 1. Делает http-запрос любого типа без параметра method
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("=== #1 ===================================================\n", response.text)

# 2. Делает http-запрос не из списка. Например, HEAD
print("=== #2 ===================================================", )
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)
response = requests.options("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)
response = requests.patch("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)

# 3. Делает запрос с правильным значением method
payload = {"method": "GET"}

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params = payload)
print("=== #3 ===================================================\n", response.text)

# 4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method
print("=== #4 ===================================================")
methods = ["POST", "GET", "PUT", "DELETE"]
for i in methods:
    r = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params ={"method": i})
    print(f"Тип запроса GET, в параметре передаем: {i}. Ответ: {r.text}")
print("======================================================")
for i in methods:
    r = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data ={"method": i})
    print(f"Тип запроса POST, в параметре передаем: {i}. Ответ: {r.text}")
print("======================================================")
for i in methods:
    r = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data ={"method": i})
    print(f"Тип запроса PUT, в параметре передаем: {i}. Ответ: {r.text}")
print("======================================================")
for i in methods:
    r = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data ={"method": i})
    print(f"Тип запроса DELETE, в параметре передаем: {i}. Ответ: {r.text}")
