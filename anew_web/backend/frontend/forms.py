from django import forms
from .models import webModels

class webForms(forms.ModelForm):
    class Meta:
        model = webModels
        fields = "__all__"