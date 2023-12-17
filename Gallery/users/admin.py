from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from cards.models import Picture


class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'nickname', 'account_image_thumb', 'account_image_counts']
    list_filter = ['user']

    def account_image_thumb(self, obj):
        return mark_safe('<a href="{}"><img src="{}" width="auto" height="50" /></a>'.format(obj.account_image.url, obj.account_image.url))

    def account_image_counts(self, obj):
        return Picture.objects.filter(author=obj.user).count()

    account_image_thumb.short_description = 'Avatar'  # Миниатюрка аватара
    account_image_counts.short_description = 'Image Counts'  # Количество загруженных пользователем изображений


admin.site.register(Account, AccountAdmin)
