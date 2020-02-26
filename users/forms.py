from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    address = forms.MultiValueField()

    class Meta:
        model = User
        fields = ['username', 'email', 'address', 'password1', 'password2']
