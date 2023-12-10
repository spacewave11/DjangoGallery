# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from cards.models import Picture


class ImageUploadForm(forms.ModelForm):
    category = forms.ChoiceField(choices=Picture.categories)
    tags = forms.CharField(max_length=100, help_text='Введите теги через запятую (до 10)')

    class Meta:
        model = Picture
        fields = ['title', 'image', 'category', 'tags']


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='Введите действительный адрес электронной почты.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким адресом электронной почты уже существует.")
        return email
