from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = [
            'first_name', 'last_name', 'profile_picture', 'username',
            'email', 'role', 'address_line1', 'city', 'state', 'pincode',
            'password1', 'password2'
        ]
        help_texts = {
            'username': None,  # Removes the help text
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES)
