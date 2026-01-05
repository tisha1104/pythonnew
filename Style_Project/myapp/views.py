from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from myapp.models import *
from django.http import JsonResponse 
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
    # Dummy cart data for demonstration
    cart_items = [
        {
            'product': {'name': 'Product 1', 'image': '/static/images/product1.jpg', 'price': 25},
            'quantity': 2,
            'get_total_price': 50
        },
        {
            'product': {'name': 'Product 2', 'image': '/static/images/product2.jpg', 'price': 15},
            'quantity': 1,
            'get_total_price': 15
        },
    ]

    cart_total = sum(item['get_total_price'] for item in cart_items)

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
    }
    return render(request, 'cart.html', context)

def details(request):
    pid=request.GET.get('pid')
    product= Product.objects.get(pk=pid)
    return render(request,'details.html',{"product":product})

def get_products(request):
    products=Product.objects.all()
    return JsonResponse({"products":list(products.values())})

def get_categories(request):
    categories=Category.objects.all()
    return JsonResponse({"categories":list(categories.values())})