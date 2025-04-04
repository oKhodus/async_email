from time import time
import requests
from async_email.tasks import send_welcome_email

url = "http://127.0.0.1:8000/register/"
data = {"username": "testuser", "email": "test@example.com", "password1": "testpass", "password2": "testpass"}

# Измеряем время выполнения HTTP-запроса
start_time = time()
response = requests.post(url, data=data)
end_time = time()

# Рассчитываем время выполнения HTTP-запроса
diff = end_time - start_time
print(f"HTTP response time: {diff:.5f} seconds")

# Запускаем отправку email асинхронно
send_welcome_email.delay(data["email"])

# Проверяем, если время выполнения HTTP-запроса меньше 1 секунды
if diff < 1:
    print("yes! :) Email was sent async (HTTP-req wasn't blocked by email sending)")
else:
    print("ioioio :( Server waited for the task to finish, Celery isn't working correctly")

