from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

import core
from accounts.models import Profile

def authenticationPage(request):
    return render(request, 'core/authenticationPage.html')  # Render the authentication page

def home_view(request):
    return render(request, 'core/home.html')  # Ensure this template exists

@csrf_protect
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email_or_phone = request.POST['email_or_phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'OOPS! Username already taken.')
                return render(request, 'core/authenticationPage.html')

            email = email_or_phone if '@' in email_or_phone else None
            if email and User.objects.filter(email=email).exists():
                messages.error(request, 'OOPS! Email already registered.')
                return render(request, 'core/authenticationPage.html')

            user = User.objects.create_user(username=username, password=password1, email=email)
            user.save()
            messages.success(request, 'Account created successfully!')
            login(request, user)
            return redirect('core:home')  # Redirect to home after signup
        else:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'core/authenticationPage.html')
    else:
        return render(request, 'core/authenticationPage.html')

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            try:
                user.profile  # Access the profile to ensure it exists
            except User.profile.RelatedObjectDoesNotExist:
                Profile.objects.create(user=user)  # Create the profile if it doesn't exist

            login(request, user)
            return redirect('core:home')  # Redirect to home after login
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'core/authenticationPage.html')
    else:
        return render(request, 'core/authenticationPage.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('core:authentication')
