from django import forms
from django.contrib.auth.models import User


def clean_email(value):
    email = value
    if User.objects.filter(email=email).exists():
        raise forms.ValidationError("Пользователь с таким адресом электронной почты уже существует.")
    return email
