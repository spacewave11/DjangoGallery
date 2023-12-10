from django import forms
from .models import Picture
from django.contrib.auth.models import User


class PictureFilterForm(forms.Form):
    categories = Picture.categories
    category_choices = [('', 'All')] + list(categories)
    category = forms.ChoiceField(choices=category_choices, required=False)
    authors = forms.ModelChoiceField(queryset=User.objects.all(), empty_label='All', required=False)
    tag_search = forms.CharField(max_length=100, required=False, label='Поиск по тегам')

    sorting_choices = [
        ('', 'Default'),
        ('date', 'Date'),
        ('downloads', 'Downloads'),
        ('rating', 'Rating'),
        ('random', 'Random'),
    ]
    sorting = forms.ChoiceField(choices=sorting_choices, required=False)
