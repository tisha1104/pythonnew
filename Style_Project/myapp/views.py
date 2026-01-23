from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from myapp.models import *
from django.http import JsonResponse ,HttpResponse
import razorpay
import datetime
from django.core.mail import send_mail
from django.conf import settings
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
    sum=0
    for c in carts:
        sum+=c.get_total_price()
    return render(request, 'cart.html',{"carts":carts,"total":int(sum)})

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
        
def removecart(request):
    cid =request.GET['cid']
    cart= Cart.objects.get(pk=cid)
    cart.delete()
    return HttpResponse("Your item in Cart Deleted Succesfully!")


def changeqty(request):
    cid =request.GET['cid']
    qty =request.GET['qty']
    cart= Cart.objects.get(pk=cid)
    if int(qty)<=0:
        cart.delete()
    else:
        cart.qty =qty
        cart.save()
    return HttpResponse("cart updated!")

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


def payment(request):
    amt = request.GET['amt']
    client = razorpay.Client(auth=("rzp_test_S1Hsg7YN8MlwDU", "ZKs1rK1XnjRDNd4uxjP2NcRJ"))

    
    data = { "amount": int(amt)*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits.
    
    return JsonResponse(payment)

def makeorder(request):
    payid=request.GET['payid']
    date = datetime.datetime.now()
    user=request.user

    carts= Cart.objects.filter(user=user)
    sum=0
    for i in carts:
        sum += i.get_total_price()

    order=Order.objects.create(user=user,data=date,total=sum,payid=payid)
    rows=""
    count=0
    for c in carts:
        OrderDetials.objects.create(order=order,product=c.product,qty=c.qty,price=c.product.price)
        rows+="<tr><td>{count}</td><td>{i.product.name}</td><td>{i.product.price}</td><td>{i.qty}</td><td>{i.get_total_price()}</td></tr>"
        c.delete()
        count+=1
        
    tbl=f"<table border='1'><thead><tr><th>PayID:{order.payid}</th></tr><tr><th>PayType:{order.paytype}</th></tr><tr><th>Order Date:{order.data}</th></tr><tr><th>Status:{order.status}</th></tr><tr><th>Total:{order.total}</th></tr><tr><th>ID</th><th>Name</th><th>Price</th><th>QTY</th><th>total</th></tr></thead><tbody>{rows}</tbody></table>"
    
                   
                    
                    
                
    
    try:
        send_mail("Order Conformation", "Your Order Placed successfully", settings.EMAIL_HOST_USER, [user.email],html_message=tbl)

    except Exception as e:
                print(e)
    return HttpResponse("order placed successfully!")

def my_orders(request):
    orders =Order.objects.filter(user=request.user)
    return render(request, 'my_orders.html',{"orders":orders})

