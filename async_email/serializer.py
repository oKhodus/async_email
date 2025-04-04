from django.contrib.auth import get_user_model
from rest_framework import serializers
from async_email.tasks import send_welcome_email

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_welcome_email.delay(user.email)  # Вызываем Celery задачу
        return user
