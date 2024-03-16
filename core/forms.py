from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *


class ToDoForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'add-search'}))

    class Meta:
        model = ToDo
        fields = ['title']


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))