from typing import Any
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms




class SignUpForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'formInput',
        'type': 'text',
        'placeholder': 'Enter Username',
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'formInput',
        'type': 'email',
        'placeholder': 'Enter Email',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'formInput',
        'type': 'password',
        'placeholder': 'Enter Password',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'formInput',
        'type': 'password',
        'placeholder': 'Enter Password',
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
