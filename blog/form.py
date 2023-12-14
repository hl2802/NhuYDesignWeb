from typing import Any
from django import forms
from .models import commentForm
class comment_Form(forms.ModelForm):

    class Meta:
            model = commentForm
            fields = ['name', 'email', 'body']