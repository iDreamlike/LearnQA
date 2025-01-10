from json.decoder import JSONDecodeError
import requests

# === 1 =============================================================================================
# response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "User"})
# parsed_response_text = response.json()
# print(parsed_response_text["answer"])
# print(parsed_response_text)
#
# print(response.text)


# === 2 =============================================================================================
# response = requests.get("https://playground.learnqa.ru/api/get_text")
# print(response.text)
#
# try:
#     parsed_response_text2 = response.json()
#     print(parsed_response_text2)
# except JSONDecodeError:
#     print("Response is not a JSON format")


# === 3 =============================================================================================
# response = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1": "value1"})
# print(response.text)
# response = requests.put("https://playground.learnqa.ru/api/check_type", data={"param2": "value2"})
# print(response.text)


# === 4 =============================================================================================
# response = requests.get("https://playground.learnqa.ru/api/check_type")
# print(response.status_code)
#
# response2 = requests.get("https://playground.learnqa.ru/api/get_500")
# print(response2.status_code)
# print(response2.text)
#
# response3 = requests.get("https://playground.learnqa.ru/api/something")
# print(response3.status_code)
# print(response3.text)

# response4 = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
# print(response4.status_code)
# print(response4.text)

# response5 = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
# first_response = response5.history[0]
# second_response = response5
#
# print(first_response.url)
# print(second_response.url)


# === 5 =============================================================================================
# headers = {"some_header": "123"}
# response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers = headers)
#
# print(response.text)
# print(response.headers)


# === 6 =============================================================================================
# payload = {"login": "secret_login", "password": "secret_pass"}
# response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
#
# print(response.text)
# print(response.status_code)
# print(dict(response.cookies))
# print(response.headers)


# === 7 =============================================================================================
payload = {"login": "secret_login", "password": "secret_pass"}

response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
cookie_value = response1.cookies.get('auth_cookie')
cookies = {}
if cookie_value is not None:
    cookies.update({'auth_cookie': cookie_value})


response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies = cookies)

print(response2.text)
