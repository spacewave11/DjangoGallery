
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required  # Добавляем декоратор
from .models import *
from .forms import ImageUploadForm


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')  # Измените 'home' на ваш URL-паттерн для главной страницы
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def index(request):
    print(request.user, request.user.id)
    user_acc = Account.objects.get(user=request.user)
    print(user_acc.nickname)
    return HttpResponse('Приложение Users')


@login_required  # Используем декоратор для обеспечения аутентификации пользователя
def upload_image(request):
    try:
        # Проверяем, есть ли у пользователя профиль Account
        user_acc = request.user.account
    except Account.DoesNotExist:
        # Если нет, создаем новый профиль
        user_acc = Account.objects.create(user=request.user, nickname=request.user.username)

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES, instance=user_acc)
        if form.is_valid():
            form.save()
            return redirect('home')  # или куда угодно после успешной загрузки
    else:
        form = ImageUploadForm(instance=user_acc)
    return render(request, 'users/upload_image.html', {'form': form})



# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES, instance=request.user.account)
#         if form.is_valid():
#             form.save()
#             return redirect('home')  # или куда угодно после успешной загрузки
#     else:
#         form = ImageUploadForm(instance=request.user.account)
#     return render(request, 'users/upload_image.html', {'form': form})