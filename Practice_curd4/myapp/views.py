from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="login")
def index(request):
    students=student.objects.all()
    if request.method=='POST':
        name= request.POST['name']
        email= request.POST['email']
        age= request.POST['age']
        image= request.FILES.get('image')
        student.objects.create(name=name,email=email,age=age,image=image)
        return render (request,"index.html",{"msg":"student register succesfully","students":students})
    else:
        return render(request,"index.html",{"students":students})


@login_required(login_url="login")
def delete_student(request):
    id=request.GET['id']
    st=student.objects.get(pk=id)
    st.delete()
    return redirect("index")


@login_required(login_url="login")
def edit_student(request):
    students=student.objects.all()
    if request.method=='POST':
        id= request.POST['id']
        name= request.POST['name']
        email= request.POST['email']
        age= request.POST['age']
        st=student.objects.get(pk=id)
        st.name=name
        st.email=email
        st.age=age
        if request.FILES:
            st.image=request.FILES.get('image')
        st.save()
        return render(request,"index.html",{"students":students})
    else:
        id=request.GET['id']
        st=student.objects.get(pk=id)
        return render(request,"index.html",{"students":students,"st":st})
    

def student_registration(request):
    if request.method=="POST":
        fname= request.POST['fname']
        lname= request.POST['lname']
        username= request.POST['username']
        password= request.POST['password']
        u= User(first_name=fname,last_name=lname,username=username)
        u.set_password(password)
        u.save()
        return render(request,"registration.html",{"msg":"Your Registration Succesfully Done!"})
    
    return render(request,"registration.html")

def student_login(request):
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']
        u= authenticate(username=username,password=password)
        if u is None:
            return render(request,"login.html",{'err':"Invalid creditional"})
        else:
            login(request,u)
            return redirect("index")
        
    return render(request,"login.html")

def user_logout(request):
    logout(request)
    return render(request,"login.html")


