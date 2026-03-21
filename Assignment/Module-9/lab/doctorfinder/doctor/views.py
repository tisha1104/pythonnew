from django.shortcuts import render,redirect
from .models import *

def home(request):
    return render(request, 'home.html')

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})

def contact(request):
    return render(request, 'contact.html')

def add_doctor(request):
    if request.method == "POST":
        name = request.POST['name']
        Doctor.objects.create(name=name)
        return redirect('/doctors/')
    return render(request, 'add.html')