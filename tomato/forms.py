from typing import Any
from django import forms
from .models import *
from django.contrib.auth.hashers import make_password


class User_register_form(forms.ModelForm):
    class Meta:
        model=New_user
        fields=['username','first_name','last_name','email','password','user_phone','user_address']

    def save(self):
        s=super().save(commit=False)
        s.password=make_password(self.cleaned_data['password'])
        s.save()
        return s


class User_login_form(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput())