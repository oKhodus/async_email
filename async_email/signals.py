from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_welcome_email
from django.contrib.auth.models import User


@receiver(post_save, sender="User")
def send_email_on_user_creation(sender, instance, created, **kwargs):
    if created:
        email = instance.email
        send_welcome_email.delay(instance.email)  # Асинхронный вызов задачи
