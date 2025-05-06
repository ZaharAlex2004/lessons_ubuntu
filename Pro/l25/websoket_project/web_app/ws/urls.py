from django.urls import path

from .consumers import ChatConsumer

socket_urlpatterns = [path('ws/chat/', ChatConsumer.as_asgi())]