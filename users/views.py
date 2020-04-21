#Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Exeption
from django.db.utils import IntegrityError
# Models
from django.contrib.auth.models import User
from users.models import Profile

# Create your views here.

# login to view feed
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})
    return render(request, 'users/login.html')

# Sign Up
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Passwords does not match'})

        # Create a new user
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'This username is already in use!'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        # Create a new profile
        profile = Profile(user=user)
        profile.save()
        
        return redirect('login')

    return render(request, 'users/signup.html')

# logout
@login_required # the user must be logged in
def logout_view(request):
    logout(request)
    return redirect('login')

