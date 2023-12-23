from django import forms
from .models import Picture
from django.contrib.auth.models import User


class PictureFilterForm(forms.Form):
    categories = Picture.categories
    category_choices = [('', 'Все категории')] + list(categories)
    category = forms.ChoiceField(choices=category_choices, required=False, label='Категории')
    authors = forms.ModelChoiceField(queryset=User.objects.all(), empty_label='Все авторы', required=False, label='Авторы')
    tag_search = forms.CharField(max_length=100, required=False, label='Поиск по тегам')

    sorting_choices = [
        ('', 'Умолчанию'),
        ('date', 'Дате'),
        ('downloads', 'Скачиваниям'),
        ('rating', 'Рейтингу'),
        ('random', 'Случайно'),
    ]
    sorting = forms.ChoiceField(choices=sorting_choices, required=False, label='Сортировать по')


class SandboxFilterForm(forms.Form):
    categories = Picture.categories
    category_choices = [('', 'Все категории')] + list(categories)
    category = forms.ChoiceField(choices=category_choices, required=False, label='Категории')
    authors = forms.ModelChoiceField(queryset=User.objects.all(), empty_label='Все авторы', required=False, label='Авторы')
    status_choices = [
        ('', 'Все'),
        ('verified', 'Проверенные'),
        ('unverified', 'На модерации'),
    ]
    status = forms.ChoiceField(choices=status_choices, required=False, label='Статус')
    tag_search = forms.CharField(max_length=100, required=False, label='Поиск по тегам')

    sorting_choices = [
        ('', 'Умолчанию'),
        ('date', 'Дате'),
        ('downloads', 'Скачиваниям'),
        ('rating', 'Рейтингу'),
        ('random', 'Случайно'),
    ]
    sorting = forms.ChoiceField(choices=sorting_choices, required=False, label='Сортировать по')


class PictureStatusForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['is_verified']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_verified'].widget.attrs.update({'class': 'form-check-input toggle-switch'})
        self.fields['is_verified'].label = ''
