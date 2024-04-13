from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from blog.models import Tag,Categorys







def register(request):
    tags = Tag.objects.all()
    category = Categorys.objects.all()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            new_user = form.save()
            print("User created successfully:", new_user)  # Debug statement
            messages.success(request, f'Hello {username} your account was created!!')

            if 'remember' in request.POST:
                request.session.set_expiry(60 * 60 * 24 * 14)  # Extend session expiry to 14 days

            # Automatically Log In The User
            new_user = authenticate(username=username, password=password1)
            if new_user is not None:
                print("User authenticated successfully:", new_user)  # Debug statement
                login(request, new_user)
                # Redirect to the desired page after successful registration
                return redirect('index')  # Change 'index' to your desired page name
            else:
                print("Authentication failed")  # Debug statement
        else:
            # Form is invalid, handle the case where the email already exists
            if User.objects.filter(email=request.POST.get('email')).exists():
                messages.warning(request, 'Email already exists! Please login.')
                return redirect('login')  # Redirect to login page if email already exists
    else:
        # GET request or form is invalid, render the registration form
        if request.user.is_authenticated:
            messages.warning(request, "Logged in Successfully...")
            return redirect('index')  # Redirect to index if user is already logged in
        else:
            form = UserRegisterForm()
            
        context = {
            'form': form,
            'tags': tags,
            'category': category,
        }
    return render(request, 'signup.html', context)


def signout(request):
    tags = Tag.objects.all()
    category = Categorys.objects.all()
    logout(request)
    messages.success(request, 'you are now signed out')
    
    # Define your context dictionary
    context = {
        'tags': tags,
        'category': category,
    }
    
    # Pass the context to the template
    return render(request, 'login.html', context)