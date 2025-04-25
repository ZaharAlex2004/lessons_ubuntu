from django.db import models
from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(),
        }
