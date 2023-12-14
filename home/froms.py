from django import forms
from .models import subForm

class contact_Form(forms.ModelForm):
    class Meta:
        model = subForm
        fields = ['email']