from django.core.mail import send_mail
from django.test import TestCase

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'your_project_name.settings'

class UserSignUpTest(TestCase):
    def test_email_sent_on_signup(self):
        # Симулируем регистрацию пользователя
        response = self.client.post('/register/', data={'email': 'test@example.com', 'password': 'securepassword'})
        
        # Проверяем, что email был отправлен
        self.assertEqual(len(send_mail), 1)  # Проверяем, что один email был отправлен
        self.assertEqual(send_mail[0].subject, 'Welcome!')  # Проверяем тему письма
        self.assertEqual(send_mail[0].to, ['test@example.com'])  # Проверяем, что email был отправлен на правильный адрес
