from django import forms
from .models import Subscription,Newsletter
# from models import Profile
from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EditProfileForm(forms.ModelForm):
    # picture = forms.ImageField(required=True)
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
    image = forms.ImageField(required=True)
    
    class Meta:
        model = Profile
        fields = ['username', 'email', 'image']
        
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

    

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['name', 'email']
        
        
class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']
        
        