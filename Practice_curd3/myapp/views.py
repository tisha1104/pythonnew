from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required 
# Create your views here.

def home(request):
    products=product.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        price=request.POST['price']
        qty=request.POST['qty']
        image=request.FILES['image']
        product.objects.create(name=name,price=price,qty=qty,image=image)
        return render(request,"home.html",{"msg":"DONE REGISTRARTION!","products":products})
    else:
        return render(request,"home.html",{"products":products})
    
def edit_product(request):
       products=product.objects.all()
       if request.method=='POST':
            id=request.POST['id']
            name=request.POST['name']
            price=request.POST['price']
            qty=request.POST['qty']
            p=product.objects.get(pk=id)
            p.name=name
            p.price=price
            p.qty=qty
            if request.FILES:
                 p.image=request.FILES.get('image')
            p.save()
            return render (request,"home.html",{"products":products,"p":p})
       else:
            id=request.GET['id']
            p=product.objects.get(pk=id)
            return render(request,"home.html",{"p":p,"products":products})
       
def delete_product(request):
     id=request.GET['id']
     p=product.objects.get(pk=id)
     p.delete()
     return redirect("home")
        
def user_registration(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lanme=request.POST['lname']
        username=request.POST['username']
        password=request.POST['password']
        
        if User.objects.filter(username=username).exists():
            return render (request,"registration.html",{"error":"Useralraday exits"})
        else:
            u=User(first_name=fname,last_name=lanme,username=username)
            u.set_password(password)
            u.save()
            return render(request,"registration.html",{"title":"registration succcesfully"})
    
    return render(request,"registration.html")

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        u=authenticate(username=username,password=password)
        if u is None:
            return render(request,"registration.html",{"err":"Invalid credtinal"})
        else:
            login(request,u)
            return redirect("home")
        
    return render(request,"login.html")

def user_logout(request):
    logout(request)
    return render(request,"login.html")