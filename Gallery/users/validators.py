from django import forms
from django.contrib.auth.models import User


def clean_email(value):
    email = value
    if User.objects.filter(email=email).exists():
        raise forms.ValidationError("Пользователь с таким адресом электронной почты уже существует.")
    return email


def validate_tags(value):
    tags = [tag.strip() for tag in value.split(',') if tag.strip()]

    if len(tags) > 10:
        raise ValidationError('Вы можете указать не более 10 тегов.')

    # for tag in tags:
    #     if not tag or tag.isspace():
    #         raise ValidationError('Тег не может быть пустым или состоять только из пробелов.')
