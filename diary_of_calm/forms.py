from django import forms
from .models import DiEntry

class DiEntryForm(forms.ModelForm):
    class Meta:
        model = DiEntry
        fields = ['title','content']