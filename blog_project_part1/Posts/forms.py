from django import forms
from .models import Posts
class AuthorForm(forms.ModelForm):
    class Meta:
        model=Posts
        exclude=['author']
        