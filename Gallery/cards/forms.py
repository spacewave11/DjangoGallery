from django import forms
from .models import Picture


class PictureFilterForm(forms.Form):
    categories = Picture.categories
    category_choices = [('', 'All')] + list(categories)
    category = forms.ChoiceField(choices=category_choices, required=False)
