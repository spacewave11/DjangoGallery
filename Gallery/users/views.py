from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ImageUploadForm, RegistrationForm, AvatarUploadForm
from cards.models import Picture, Tag


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('cards_index')
    else:
        form = RegistrationForm()
    context = {'form': form, 'active_page': 'register'}
    return render(request, 'users/register.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('cards_index')
    else:
        form = AuthenticationForm()
    context = {'form': form, 'active_page': 'login'}
    return render(request, 'users/login.html', context)


def index(request):
    print(request.user, request.user.id)
    user_acc = Account.objects.get(user=request.user)
    print(user_acc.nickname)
    return HttpResponse('Приложение Users')


@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user_acc = request.user.account
            except Account.DoesNotExist:
                user_acc = Account.objects.create(user=request.user, nickname=request.user.username)

            picture = form.save(commit=False)
            picture.author = request.user
            picture.rating = 0
            picture.downloads = 0
            picture.save()
            picture.category = form.cleaned_data['category']

            tags_input = form.cleaned_data['tags']
            tags_list = [tag.strip() for tag in tags_input.split(',')]
            for tag_title in tags_list:
                tag, created = Tag.objects.get_or_create(title=tag_title)
                picture.tags.add(tag)

            return redirect('cards_index')
    else:
        form = ImageUploadForm()
    context = {'form': form, 'active_page': 'upload_image'}
    return render(request, 'users/upload_image.html', context)


@login_required
def profile(request):
    user = request.user
    all_uploaded_images = Picture.objects.filter(author=user).order_by('-date')

    try:
        account = user.account
    except Account.DoesNotExist:
        account = Account.objects.create(user=user, nickname=user.username)

    if request.method == 'POST':
        form = AvatarUploadForm(request.POST, request.FILES)
        if form.is_valid():
            account.account_image = form.cleaned_data['avatar']
            account.save()
            return redirect('profile')
    else:
        form = AvatarUploadForm()
    context = {'user': user, 'uploaded_images': all_uploaded_images, 'form': form, 'active_page': 'profile'}
    return render(request, 'users/account.html', context)
