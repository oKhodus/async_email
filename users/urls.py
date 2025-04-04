# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('async-home/', views.register_user, name='async_home'),  # Асинхронное представление
]
