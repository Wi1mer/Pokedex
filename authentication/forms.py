from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .models import CustomUser

#  Estilos para los formularios

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label=_("User"),
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'username', "autofocus": True})
        )
    email = forms.CharField(
        label=_("Email"),
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'name@example.com'})
        )
    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', "autocomplete": "new-password"})
        )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', "autocomplete": "new-password"})
        )

    class Meta:
        model = CustomUser
        fields = ("username", "email")

        

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label=f"{_('Email')} / {_('User')}",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'name@example.com'})
        )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        )