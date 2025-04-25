from datetime import date

from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.shortcuts import render
from django.contrib.auth import login
from .tasks import send_registration_email, send_promotional_email
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone


def home_view(request: HttpRequest) -> render:
    """
    Главная страница.
    :param request: HttpRequest
    :return: render
    """
    today = date.today()
    return render(request, 'celer/home.html', {'today': today})


def register(request):
    """Регистрация нового пользователя и отправка имейлов."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            send_registration_email.apply_async(args=[user.email])

            send_promotional_email.apply_async(args=[user.email], countdown=600)

            return JsonResponse({"message": "Реєстрація успішна"}, status=201)
        return JsonResponse({"errors": form.errors}, status=400)

    else:
        form = UserCreationForm()

    return render(request, 'celer/register.html', {'form': form})

def test_celery_task(request):
    send_registration_email.delay('test@example.com')
    return JsonResponse({'status': 'task sent'})
