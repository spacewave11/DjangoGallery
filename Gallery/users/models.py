# users/models.py
from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nickname = models.CharField(max_length=100)
    account_image = models.ImageField(default='default.jpg', upload_to='account_images')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.user.username}'s account"
