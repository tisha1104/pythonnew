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
from django.contrib import messages
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
    category = Category.objects.get(name__iexact='jewellery')
    products = Product.objects.filter(category=category)
    return render(request, 'jewellery.html', {'products': products})


@login_required(login_url="login_register")
def fashion(request):
    products = Product.objects.filter(category__name="Fashion")
    return render(request, 'fashion.html', {'products': products})

@login_required(login_url="login_register")
def electronic(request):
    products = Product.objects.filter(category__name="Electronic")
    return render(request, 'electronic.html', {'products': products})

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


# @login_required(login_url="login_register")
# def cart_view(request):
#     carts=Cart.objects.filter(user=request.user)
#     sum=0
#     for c in carts:
#         sum+=c.get_total_price()
#     return render(request, 'cart.html',{"carts":carts,"total":int(sum)})

@login_required(login_url="login_register")
def cart_view(request):
    carts = Cart.objects.filter(user=request.user)
    total = sum(i.get_total_price() for i in carts)
    addresses = Address.objects.filter(user=request.user)

    return render(request, 'cart.html', {
        'carts': carts,
        'total': int(total),
        'addresses': addresses
    })


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
    q=request.GET.get('q','')
    products = Product.objects.filter(name__icontains=q)
    return JsonResponse({"products":list(products.values())})



def payment(request):
    if request.method == "POST":
        amt = request.POST.get("amt")

        client = razorpay.Client(auth=(
            "rzp_test_SF5R7ur5nvvYLR",   
            "NgUDBnx9JpMGHTWixBznB0S3"        
        ))

        data = {
            "amount": int(float(amt)) * 100, 
            "currency": "INR",
            "receipt": "order_rcptid_11"
        }

        order = client.order.create(data=data)

        return JsonResponse(order)

# def makeorder(request):
#     try:
#         payid = request.GET.get('payid')
#         adr_id = request.GET.get('adr')

#         adr = Address.objects.get(id=adr_id)
#         user = request.user
#         date = datetime.datetime.now()

#         carts = Cart.objects.filter(user=user)

#         total = sum(i.get_total_price() for i in carts)

#         order = Order.objects.create(
#             user=user,
#             data=date,
#             total=total,
#             payid=payid,
#             paytype="Razorpay",
#             address=adr,
#             status="Placed"
#         )

#         rows = ""
#         count = 1

#         for c in carts:
#             OrderDetials.objects.create(
#                 order=order,
#                 product=c.product,
#                 qty=c.qty,
#                 price=c.product.price
#             )

#             rows += f"""
#             <tr>
#                 <td>{count}</td>
#                 <td>{c.product.name}</td>
#                 <td>{c.product.price}</td>
#                 <td>{c.qty}</td>
#                 <td>{c.get_total_price()}</td>
#             </tr>
#             """
#             c.delete()
#             count += 1

#         html = f"""
#         <h3>Delivery Address</h3>
#         <p>{adr.address}</p>

#         <table border="1" cellpadding="5">
#             <tr><th colspan="5">Payment ID: {order.payid}</th></tr>
#             <tr>
#                 <th>#</th><th>Name</th><th>Price</th><th>Qty</th><th>Total</th>
#             </tr>
#             {rows}
#         </table>
#         <h4>Total Amount: ₹{order.total}</h4>
#         """

#         send_mail(
#             "Order Confirmation",
#             "Your order placed successfully",
#             settings.EMAIL_HOST_USER,
#             [user.email],
#             html_message=html
#         )

#         return HttpResponse("Order placed successfully!")

#     except Exception as e:
#         print("ORDER ERROR:", e)
#         return HttpResponse("Order failed")



def makeorder(request):

    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=400)

    payid = request.POST.get('payid')
    adr_id = request.POST.get('adr')

    if not payid:
        return JsonResponse({"error": "Payment ID missing"}, status=400)

    if not adr_id:
        return JsonResponse({"error": "Address not selected"}, status=400)

    try:
        adr = Address.objects.get(pk=adr_id)
    except Address.DoesNotExist:
        return JsonResponse({"error": "Invalid address"}, status=400)

    user = request.user
    date = datetime.datetime.now()

    carts = Cart.objects.filter(user=user)

    if not carts.exists():
        return JsonResponse({"error": "Cart is empty"}, status=400)

    total_amount = 0
    for i in carts:
        total_amount += i.get_total_price()

    # Create Order
    order = Order.objects.create(
        user=user,
        data=date,
        total=total_amount,
        payid=payid,
        address=adr
    )

    rows = ""
    count = 1

    for c in carts:
        OrderDetials.objects.create(
            order=order,
            product=c.product,
            qty=c.qty,
            price=c.product.price
        )

        rows += f"""
        <tr>
            <td>{count}</td>
            <td>{c.product.name}</td>
            <td>{c.product.price}</td>
            <td>{c.qty}</td>
            <td>{c.get_total_price()}</td>
        </tr>
        """

        c.delete()
        count += 1

    # Email Table
    tbl = f"""
    <h3>Delivery Address</h3>
    <p>{adr.address}</p>

    <table border='1'>
        <thead>
            <tr><th colspan='5'>PayID: {order.payid}</th></tr>
            <tr><th colspan='5'>Order Date: {order.data}</th></tr>
            <tr><th colspan='5'>Total: ₹{order.total}</th></tr>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Price</th>
                <th>QTY</th>
                <th>Total</th>
            </tr>
        </thead>
        <tbody>
            {rows}
        </tbody>
    </table>
    """

    try:
        send_mail(
            "Order Confirmation",
            "Your order placed successfully",
            settings.EMAIL_HOST_USER,
            [user.email],
            html_message=tbl
        )
    except Exception as e:
        print("Email Error:", e)

    return JsonResponse({"success": "Order placed successfully"})

@login_required(login_url="login_register")
def my_orders(request):
    orders =Order.objects.filter(user=request.user)
    return render(request, 'my_orders.html',{"orders":orders})

def address(request):
    return render(request,"address.html")

@login_required(login_url="login_register")
def add_address(request):
    user=request.user
    adr=request.GET.get('address')
    Adr=Address.objects.create(user=user,address=adr)
    return HttpResponse("Successfully added Address!")

def get_addresses(request):
    address=Address.objects.filter(user=request.user)
    return JsonResponse({'adr':list(address.values())})

def forgotpass(request):
    return render(request,"forgot.html")

def password_sendemail(request):
    email=request.POST['email']
    try:
        user= User.objects.get(email=email)
        send_mail("Password Recovery", f"http://127.0.0.1:8000/resetpass?email={email}",
        settings.EMAIL_HOST_USER, [email])

        return render(request,"forgot.html",{"err":"Email Sent Successfully!"})
    except Exception as e:
        return render(request,"forgot.html",{"err":"Something Went Wrong!"})
    
def resetpass(request):
    if request.method=='GET':
        email=request.GET['email']
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.get(email=email)
        user.set_password(password)
        user.save()
        

    return render(request,"resetpass.html",{"email":email})

@login_required(login_url="login_register")
def delete_address(request):
    id=request.GET['id']
    adr=Address.objects.get(pk=id)
    adr.delete()
    return HttpResponse("Your Address Deleted uccesfully!")

@login_required(login_url="login_register")
def update_address(request):
    if request.method == "POST":
        id = request.POST.get('id')
        address = request.POST.get('address')

        try:
            adr = Address.objects.get(pk=id, user=request.user)
            adr.address = address
            adr.save()
            return HttpResponse("Your Address Updated Successfully!")
        except Address.DoesNotExist:
            return HttpResponse("Address Not Found")

    return HttpResponse("Invalid Request")


@login_required(login_url="login_register")
def user_profile(request):
    profile, created = Userprofile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()

        image = request.FILES.get('photo')
        if image:
            profile.image = image
            profile.save()
    return render(request, 'profile.html')
   
@login_required(login_url="login_register")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        messages.success(request, "Message sent successfully!")

    return render(request, "contact.html")

