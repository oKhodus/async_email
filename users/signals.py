from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from async_email.tasks import send_welcome_email

@receiver(post_save, sender=User)
def send_welcome_email_signal(sender, instance, created, **kwargs):
    if created:  # Проверяем, что это новый пользователь
        send_welcome_email.delay(instance.email)  # Отправляем задачу в Celery
