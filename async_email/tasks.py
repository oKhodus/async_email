from celery import shared_task
import logging
import re

# Настройка логгера
logger = logging.getLogger(__name__)

# Функция для проверки правильности email
def is_valid_email(email):
    # Простая регулярка для проверки формата email
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email)

@shared_task
def send_welcome_email(email):
    logger.info(f"Received email: {email} (type: {type(email)})")
    
    if not isinstance(email, str):
        logger.error(f"Invalid type for email: {type(email)}")
        return f"Error: Invalid email type"

    if not is_valid_email(email):
        logger.error(f"Invalid email structure: {email}")
        return f"Error: Invalid email structure"

    # Логируем успешную отправку письма
    logger.info(f"Sending welcome email to: {email}")
    
    # Здесь будет код для отправки email
    return f"Welcome email is delivered to the user"


