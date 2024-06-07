from django import forms
from .models import Musician, Album
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']



class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'instrument_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'first_name', 'last_name', 'email', 'phone_number', 'instrument_type',
            Submit('submit', 'Save', css_class='btn-primary')
        )

class AlbumForm(forms.ModelForm):
    rating = forms.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        widget=forms.NumberInput(attrs={'min': '1', 'max': '5'})
    )

    class Meta:
        model = Album
        fields = ['name', 'musician', 'release_date', 'rating']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name', 'musician', 'release_date', 'rating',
            Submit('submit', 'Save', css_class='btn-primary')
        )