from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from myapp.models import *
from django.http import JsonResponse ,HttpResponse
# Create your views here.

def index(request):
    if request.GET:
        cid=request.GET['cid']
        products=Product.objects.filter(category_id=cid)
    else:
        products=Product.objects.all()
    categories= Category.objects.all()
    return render(request,'index.html',{"products":products,"categories":categories})

@login_required(login_url="login_register")
def jewellery(request):
    return render(request,'jewellery.html')

@login_required(login_url="login_register")
def fashion(request):
    return render(request,'fashion.html')

@login_required(login_url="login_register")
def electronic(request):
    return render(request,'electronic.html')

def user_regierstation(request):
    if request.method=='POST':
        data = request.POST
        fname =data.get('fname')
        lname= data.get('lname')
        username=data.get('username')
        password=data.get('password')


        if User.objects.filter(username=username).exists():
            return render (request,"login_register.html",{"title":"User alredy exits!"})

        u= User(first_name=fname,last_name=lname,username=username)
        u.set_password(password)
        u.save()
        return render(request,"login_register.html",{"msg":"Regierstation Successfully Done!"})
    
def login_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "login_register.html", {"err": "Invalid credentials"})

    return render(request, "login_register.html")

def user_logout(request):
    logout(request)
    return redirect("index")


@login_required(login_url="login_register")
def cart_view(request):
    carts=Cart.objects.filter(user=request.user)
    return render(request, 'cart.html',{"carts":carts})

def addtocart(request):
    pid = request.GET['pid']
    product=Product.objects.get(pk=pid)
    user = request.user

    if user.is_anonymous:
        return HttpResponse(user)
    else:
        isexist=Cart.objects.filter(user=user,product=product)
        if(len(isexist)>=1):
            isexist[0].qty=isexist[0].qty+1
            isexist[0].save()
            return HttpResponse("Your Product Succesfully Added Into Cart!")

        else:
            Cart.objects.create(product=product,user=user,qty=1)
            return HttpResponse("Your Product Succesfully Added Into Cart!")

def details(request):
    pid=request.GET.get('pid')
    product= Product.objects.get(pk=pid)
    return render(request,'details.html',{"product":product})

def get_products(request):
    catid=request.GET['catid']
    if int(catid)>0:
       products=Product.objects.filter(category_id=catid)
    else:
        products=Product.objects.all()
        
    return JsonResponse({"products":list(products.values())})

def get_categories(request):
    categories=Category.objects.all()
    return JsonResponse({"categories":list(categories.values())})

def search_product(request):
    q=request.GET['q']
    products=Product.objects.filter(name__startswith=q)
    return JsonResponse({"products":list(products.values())})