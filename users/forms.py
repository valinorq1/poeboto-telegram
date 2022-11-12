from typing import Dict, Any

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from core import mixins as custom_mixins


class RegisterUserForm(custom_mixins.AddClassNameMixin, forms.Form):
    email = forms.EmailField(label='Почта',widget=forms.EmailInput())
    password1 = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'id':'password1'}))
    password2 = forms.CharField(label='Пароль ещё раз',widget=forms.PasswordInput(attrs={'id':'password2'}))

    def clean(self) -> Dict:
        cleaned_data = super().clean()

        if cleaned_data['password1'] != cleaned_data['password2']:
            raise ValidationError('Passwords do not match!')

        return cleaned_data

    def clean_email(self) -> Any:
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise ValidationError('This email is already taken!')

        return email


class LoginUserForm(custom_mixins.AddClassNameMixin, forms.Form):
    email = forms.EmailField(label="Почта", widget=forms.EmailInput())
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    remember_me = forms.BooleanField(label='Запомнить меня?',widget=forms.CheckboxInput(attrs={'id':'flexCheckDefault'}), required=False)
