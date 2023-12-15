from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class AccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'nickname', 'account_image_thumb']
    list_filter = ['user']

    def account_image_thumb(self, obj):
        return mark_safe('<a href="{}"><img src="{}" width="auto" height="50" /></a>'.format(obj.account_image.url, obj.account_image.url))

    account_image_thumb.short_description = 'Avatar'  # Миниатюрка аватара


admin.site.register(Account, AccountAdmin)
