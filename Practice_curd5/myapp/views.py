from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login') 
def home(request):
    productes=product.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        price=request.POST['price']
        qty=request.POST['qty']
        image=request.FILES['image']
        product.objects.create(name=name,price=price,qty=qty,image=image)
        return render(request,"home.html",{"productes":productes,"msg":"PRODUCT INSERT SUCCESSFULLY!"})
    else:
        return render(request,"home.html",{"productes":productes})
@login_required(login_url='login') 
def edit_product(request):
    productes=product.objects.all()
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
            p.image=request.FILES['image']
        p.save()
        return render(request,"home.html",{"productes":productes})
    else:
            id=request.GET['id']
            p=product.objects.get(pk=id)
            return render(request,"home.html",{"p":p,"productes":productes})
    
@login_required(login_url='login') 
def delete_product(request):
    id=request.GET['id']
    p=product.objects.get(pk=id)
    p.delete()
    return redirect("home")


def ragistation(request):
    if request.method=='POST':
          fname=request.POST['fname']
          lname=request.POST['lname']
          username=request.POST['username']
          password=request.POST['password']
          
          if User.objects.filter(username=username).exists():
               return render(request,"ragistation.html",{"err":"USER ALREADY EXITS!"})
          else:
            u=User.objects.create(first_name=fname,last_name=lname,username=username)
            u.set_password(password)
            u.save()
            return render(request,"ragistation.html",{"mesges":"ragistation succesfully!"})
    return render(request,"ragistation.html")

def login_data(request):
    if request.method=='POST':
        username=request.POST['username']
        passsword=request.POST['password']
       
        u=authenticate(username=username,password=passsword)
        
        print(u)
        if u is None:
            return render(request,"login.html",{"msg":"Invalid DATA!"})
        else:
            login(request,u)
            return redirect('home')

    return render(request,"login.html")

def logout_data(request):
    logout(request)
    return render(request,"login.html")