from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class PictureAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_thumb', 'author', 'date', 'category', 'downloads', 'rating']
    list_filter = ['category', 'author', 'date']
    ordering = ['-date', 'rating', 'downloads']

    def image_thumb(self, obj):
        return mark_safe('<a href="{}"><img src="{}" width="auto" height="50" /></a>'.format(obj.image.url, obj.image.url))

    image_thumb.short_description = 'Thumb'  # Миниатюра


class TagAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']


admin.site.register(Picture, PictureAdmin)
admin.site.register(Tag, TagAdmin)
