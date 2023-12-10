from django import forms
from .models import Picture
from django.contrib.auth.models import User


class PictureFilterForm(forms.Form):
    categories = Picture.categories
    category_choices = [('', 'All')] + list(categories)
    category = forms.ChoiceField(choices=category_choices, required=False)
    authors = forms.ModelChoiceField(queryset=User.objects.all(), empty_label='All', required=False)

    sorting_choices = [
        ('', 'Default'),
        ('date', 'Date'),
        ('downloads', 'Downloads'),
        ('rating', 'Rating'),
        ('random', 'Random'),
    ]
    sorting = forms.ChoiceField(choices=sorting_choices, required=False)

