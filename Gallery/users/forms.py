from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cards.models import Picture
from .validators import clean_email


class ImageUploadForm(forms.ModelForm):
    category = forms.ChoiceField(choices=Picture.categories)
    tags = forms.CharField(max_length=100, help_text='Введите теги через запятую (до 10)')

    class Meta:
        model = Picture
        fields = ['title', 'image', 'category', 'tags']


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='Введите действительный адрес электронной почты.', validators=[clean_email])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AvatarUploadForm(forms.Form):
    avatar = forms.ImageField()