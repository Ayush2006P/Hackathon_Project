from django.shortcuts import render, redirect
from datetime import datetime
from userapp.models import register
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Store user in custom register model (not secure for real projects)
        usersignup = register(firstName=firstName, lastName=lastName, email=email, password=password, date=datetime.today())
        usersignup.save()

        messages.success(request, "You are signed in NOW!")  
        return redirect('login')  # Redirect to login page after signup

    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Check credentials manually (since `register` is not Django's User model)
            user = register.objects.get(email=email, password=password)
            messages.success(request, "Login successful!")
            return redirect('home')
        except register.DoesNotExist:
            messages.warning(request, "Invalid Email or Password!")
            return redirect('login')

    return render(request, 'login.html')
