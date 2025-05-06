from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from . import views

urlpatterns = [
    path('', home_view, name='home'),
    path('notify/', notify_group),
    path('update_company/<int:company_id>/', views.CompanyUpdateView.as_view(), name='update_company'),
    path('create_company/', views.create_company, name='create_company'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)