# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


# ALLAUTH override signup form
class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='asdf')

    def signup(self, request, user):
        user.save()
