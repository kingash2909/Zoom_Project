from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    firstname = forms.CharField(max_length=50, required = True)
    lastname = forms.CharField(max_length=50, required = True)
    email = forms.EmailField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'email', 'password1', 'password2']


    def save(self, commit: True):
        user =  super(SignUpForm,self).save(commit=False)
        user.username = self.cleaned_data['email']
        user.firstname = self.cleaned_data['firstname']
        user.lastname = self.cleaned_data['lastname']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

            return user