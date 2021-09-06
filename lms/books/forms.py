from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from .models import Books

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'password1' : forms.PasswordInput(attrs={'class':'form-control'}),
            'password2' : forms.PasswordInput(attrs={'class':'form-control'}),
        }

class AddBooks(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['name', 'author', 'ISBN', 'img']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'ISBN': forms.NumberInput(attrs={'class':'form-control'}),
        }
