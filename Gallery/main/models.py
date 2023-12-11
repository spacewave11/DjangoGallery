# from django.db import models


# class Image(models.Model):
#     user_avatar = models.ImageField(upload_to='main/avatars/', default='main/avatars/ava1.jpg')
#     user_nickname = models.CharField(max_length=100, default='Guest')
#     image = models.ImageField(upload_to='main/img/', default='main/img/picture1.jpg')
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'Image by {self.user_nickname} - {self.timestamp}'


# class Category:
#     def __init__(self, name, slug):
#         self.name = name
#         self.slug = slug