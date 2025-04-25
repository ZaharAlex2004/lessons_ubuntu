from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_registration_email(email):
    user = User.objects.get(email=email)
    send_mail(
        'Реєстрація успішна',
        f'Дякуємо за реєстрацію! Ласкаво просимо {user.username}',
        'noreply@example.com',
        [user.email],
        fail_silently=False,
    )

@shared_task
def send_promotional_email(email):
    user = User.objects.get(email=email)
    send_mail(
        'Наші можливості',
        'Знайомтесь з додатковими можливостями нашого сервісу!',
        'noreply@example.com',
        [user.email],
        fail_silently=False,
    )

@shared_task
def log_user_count():
    user_count = User.objects.count()
    print(f"Користувачів в БД: {user_count}")
