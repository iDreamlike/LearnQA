import json

from requests import get
import time


#=== 1. Создаем задачу =========================================================
r = get("https://playground.learnqa.ru/ajax/api/longtime_job")
print(f"=== 1 ================================================\n{r.text}")
job_data = json.loads(r.text)

#=== 2. Проверяем правильность ответов до выполнения задачи ====================
print(f"=== 2 ================================================")
r2 = get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": "wrong_token"})
print(r2.text)
r3 = get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": job_data["token"]})
print(r3.text)

#=== 3. Проверяем правильность ответов после выполнения задачи =================
print(f"=== 3 ================================================\nЖдем {job_data["seconds"]} секунд...")
time.sleep(job_data["seconds"])
r4 = get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": job_data["token"]})
print(r4.text)
job_data2 = json.loads(r4.text)
if job_data2["result"] and job_data2["status"] == "Job is ready":
    print("Все ОК!")
else:
    print("Что-то не так.")
