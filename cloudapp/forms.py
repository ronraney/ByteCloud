from django import forms
from django.forms import ModelForm
from .models import Byte

class ByteForm(forms.ModelForm):
    class Meta:
        model = Byte
        fields = '__all__'
        labels = {
            "text": "Choose a word or phrase"
        }