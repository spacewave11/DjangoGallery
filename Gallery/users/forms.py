
from django import forms
from .models import Account


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['image']
