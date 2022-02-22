from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms


from .forms import register_form

# Create your views here.

def register_request(request):
    if request.method == "POST":
        form = register_form(request.POST)


        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists, try logging in to an existing account.")

            else:
                user = form.save()
                login(request, user)
                messages.success(request, "Registration successful.")
                return redirect("/")

        messages.error(request, "Unsuccessful registration. Invalid information.")

    else:
        form = register_form()

    return render(request, 'users/register.html', {'title': 'Sign Up', 'register_form': form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    return render(request, 'users/login.html', {'title': 'Login', 'login_form': form})

# def logout_request(request):