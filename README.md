# Django Celery Async Email
This project demonstrates how to send a welcome/verification email asynchronously using Celery when a new user registers. The goal is to have the email sent in the background so that the HTTP registration endpoint returns quickly.

## Features

- **User Registration:** A Django form for user registration.
- **Asynchronous Email Sending:** Upon successful registration, a Celery task is triggered to send a welcome email without delaying the HTTP response.
- **Console Email Backend:** Uses `django.core.mail.backends.console.EmailBackend` for testing (emails are printed in the console).
- **Quick HTTP Response:** The registration endpoint responds immediately, confirming that the email logic is offloaded to Celery.

## Requirements

- Python 3.8+
- Django 5.2
- Celery 5.5.0 (or a compatible version)
- Redis (as the broker for Celery)

You can install the requirements using:

```bash
pip install -r requirements.txt

async_email/                # Root project directory
│
├── async_email/            # Django project package
│   ├── __init__.py
│   ├── settings.py         # Contains Celery and email backend configuration
│   ├── urls.py             # URL configuration for the project
│   ├── celery_config.py    # Celery configuration file
│   ├── wsgi.py
│
├── register.html
├── home.html
│
├── async_test.py           # A custom script to test asynchronous behavior
├── manage.py
└── requirements.txt

## Running the Project
1. Start Redis

- Make sure Redis is running (for example, on localhost:6379):

```bash
redis-server

2. Run Celery Worker

- In a new terminal window (from the root directory), start the Celery worker:

```bash
celery -A async_email.celery_config.app worker --pool=solo -l info

3. Run Django Server

- From the root directory, start the Django development server:

```bash
python manage.py runserver

4. Register a New User

    - Open your browser and go to: http://127.0.0.1:8000/register/

    - Fill out the registration form and submit.

    - The HTTP response should be fast (confirming that the email task is executed asynchronously).

You should see in your Celery worker logs something like:

    [INFO/MainProcess] Task async_email.tasks.send_welcome_email[...] received
    [INFO/MainProcess] Received email: test@example.com (type: <class 'str'>)
    [INFO/MainProcess] Sending welcome email to: test@example.com
    [INFO/MainProcess] Task async_email.tasks.send_welcome_email[...] succeeded in ...s: 'Welcome email is delivered to the user'

5. Run Async Test (Optional)

- You can use the provided async_test.py script to measure the HTTP response time:

```bash
python async_test.py

- This script will send a POST request to the registration endpoint and print the HTTP response time, verifying that the request is not delayed by email sending.