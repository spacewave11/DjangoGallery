from django.shortcuts import render, HttpResponse
from .models import *

def index(request):
    print(request.user, request.user.id)
    user_acc = Account.objects.get(user=request.user)
    print(user_acc.nickname)
    return HttpResponse('Приложение Users')