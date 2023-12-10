from django.contrib import admin
from .models import *


class PictureAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'author', 'date', 'category']
    list_filter = ['category', 'author', 'date']


class TagAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']


admin.site.register(Picture, PictureAdmin)
admin.site.register(Tag, TagAdmin)
