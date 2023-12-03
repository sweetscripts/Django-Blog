from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#A form for new user registration.
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#A form for updating existing users.
class UserUpdateForm(forms.ModelForm):
     email = forms.EmailField()

     class Meta:
        model = User
        fields = ['username', 'email']

# A form for updating user profiles.
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']