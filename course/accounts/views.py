from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import login,authenticate

# Create your views here.

def register_view(request):
    form = RegisterForm(request.POST or None)
    
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect('login')

    return render(request, 'accounts/register.html', {'form': form})

from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'accounts/login.html')