from django.http import JsonResponse
from async_email.tasks import send_welcome_email

def register_user(request):
    email = request.POST.get('email')
    # Логика регистрации (сохранение пользователя в базе данных)

    # Вызов асинхронной задачи Celery для отправки email
    send_welcome_email.delay(email)

    return JsonResponse({'message': 'Registration successful!'})
