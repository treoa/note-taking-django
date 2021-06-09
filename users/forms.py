from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth import password_validation


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=16, min_length=6, required=True, help_text='Required: First Name',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=16, min_length=6, required=True, help_text='Required: Last Name',
        widget=(forms.TextInput(attrs={'class': 'form-control'}))
    )
    email = forms.EmailField(
        max_length=52, help_text='Required. Inform a valid email address.',
        widget=(forms.TextInput(attrs={'class': 'form-control'}))
    )
    password1 = forms.CharField(
        label=('Password'),
        widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
        help_text=password_validation.password_validators_help_text_html()
    )
    password2 = forms.CharField(
        label=('Password Confirmation'), 
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=('Just Enter the same password, for confirmation')
    )
    username = forms.CharField(
        label=('Username'),
        max_length=152,
        help_text=('Required. 152 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={'unique': ("A user with that username already exists.")},
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)
