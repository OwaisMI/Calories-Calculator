from django import forms
from .models import *
from django.forms import ModelForm

class Cal(forms.ModelForm):
    class Meta:
        model = CalorieCal
        fields='__all__'
