from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Устанавливаем настройки Django для Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'async_email.settings')

app = Celery('async_email', broker='redis://localhost:6379/0')

# Используем настройки из settings.py с префиксом CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находим задачи в приложениях
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

# celery -A async_email worker --pool=solo -l info
