# async_email/apps.py

from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'async_email'

    def ready(self):
        import async_email.signals  # Импортируем сигнал
