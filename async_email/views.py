from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import UserRegistrationForm
from .tasks import send_welcome_email
import logging

logger = logging.getLogger(__name__)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print("Полученный email:", form.cleaned_data.get("email"))
            user = form.save()
            login(request, user)  # Аутентифицируем пользователя сразу после регистрации
            
            email = user.email
            logger.info(f"Registering user with email: {email}")
            
            if email:
                print(f"Перед отправкой email: {email}")
                send_welcome_email.delay(email)  # Отправляем email через Celery
                messages.success(request, f'Account created for {user.username}!')
            else:
                print("Email пустой перед отправкой!")

            return redirect('home')  # Перенаправляем на домашнюю страницу после регистрации
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

def home(request):
    return render(request, 'home.html')