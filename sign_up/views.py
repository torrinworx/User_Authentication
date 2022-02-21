from django.shortcuts import render, redirect
from .forms import register_form
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

def register_request(request):
    if request.method == "POST":
        form = register_form(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")

        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = register_form()
    return render(request, 'sign_up/register.html', {'title': 'Sign Up', 'register_form': form})

