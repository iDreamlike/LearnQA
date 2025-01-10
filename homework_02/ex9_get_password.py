from requests import post


passwords = ["123456", "123456789", "qwerty", "password", "1234567",
             "12345678", "12345", "iloveyou", "111111", "123123",
             "abc123", "qwerty123", "1q2w3e4r", "admin", "qwertyuiop",
             "654321", "555555", "lovely", "7777777", "welcome",
             "888888", "princess", "dragon", "password1", "123qwe"]
count = 0
for i in passwords:
    count += 1
    r = post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login": "super_admin", "password": i})
    print(f"Попытка №{count}: пробуем пароль: {i}")
    print(r.text)
    cookie_value = r.cookies.get('auth_cookie')
    r2 = post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies={"auth_cookie": cookie_value})
    print(f"{r2.text}\n")
    if r2.text == "You are authorized":
        print(f"Пароль подобран: {i}")
        break
