# from models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



        
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'prompt srch_explore'}),
        max_length=50,
        required=True
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'prompt srch_explore'}),
        max_length=50,
        required=True
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'prompt srch_explore'}),
        max_length=50,
        required=True
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'prompt srch_explore'}),
        max_length=50,
        required=True
    )
    remember = forms.BooleanField(
        label='Remember Me',
        required=False
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'remember']

    
