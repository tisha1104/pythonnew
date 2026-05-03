from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="login")
def home(request):
    student=Student.objects.all().order_by("-id")

    search=request.GET.get("search")
    if search:
        student=student.filter(name__icontains=search)

    min_price=request.GET.get("min_price")
    max_price=request.GET.get("max_prica")

    if min_price:
        student=student.filter(price__gte=min_price)

    if max_price:
        student=student.filter(price__lte=max_price)

  

    if request.method=='POST':
        name=request.POST['name']
        emial=request.POST['emial']
        sub=request.POST['sub']
        image=request.FILES['image']
        price=request.POST['price']
        Student.objects.create(name=name,emial=emial,sub=sub,image=image,price=price)
        return render(request,"home.html",{"msg":"Stuudent Data Insert Successfully!","student":student})
    else:
        return render(request,"home.html",{"student":student})
    
def delete_student(request):
    id=request.GET['id']
    s=Student.objects.get(pk=id)
    s.delete()
    return redirect("home")

def edit_student(request):
    student=Student.objects.all()
    if request.method=='POST':
        id=request.GET['id']
        name=request.POST['name']
        emial=request.POST['emial']
        sub=request.POST['sub']
        price=request.POST['price']
        s=Student.objects.get(pk=id)
        s.name=name
        s.emial=emial
        s.sub=sub
        s.price=price
        if request.FILES:
            s.image=request.FILES['image']
        s.save()
        # return render(request,"home.html",{"student":student,"s":s})
        return redirect("home")
    else:
        id=request.GET['id']
        s=Student.objects.get(pk=id)
        return render(request,"home.html",{"student":student,"s":s})
        # return redirect("home")


def registration_user(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        password=request.POST['password']
        u=User(first_name=fname,last_name=lname,username=username)
        u.set_password(password)
        u.save()
        return render(request,"registration.html",{"msg":"Registration Successfully Done!"})
    return render(request,"registration.html")

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        u=authenticate(username=username,password=password)
        if u is None:
            return render(request,"login.html",{"err":"Invalid credentials"})
        else:
            login(request,u)
            return redirect("home")
    return render (request,"login.html")

def user_logout(request):
    logout(request)
    return render(request,"login.html")