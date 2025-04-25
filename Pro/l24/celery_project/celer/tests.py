from django.http import HttpResponse
from django.test import TestCase
from .tasks import send_registration_email
from unittest.mock import patch

def test_celery_task(request):
    send_registration_email.delay('test@example.com')
    return HttpResponse("Email sent to test@example.com")
