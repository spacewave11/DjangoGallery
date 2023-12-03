# users/admin.py
from django.contrib import admin

from .models import *


class AccountAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_filter = ['user']


admin.site.register(Account, AccountAdmin)
