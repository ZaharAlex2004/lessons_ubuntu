from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('test-celery/', views.test_celery_task, name='test_celery'),
    path('register/', views.register, name='register'),
]