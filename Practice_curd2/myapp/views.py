from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.

def home(request):
    return render(request,"home.html")

def register(request):
    id= request.POST.get('id')
    name= request.POST.get('name')
    email= request.POST.get('email')
    age= request.POST.get('age')
    image= request.FILES.get('image')
    if not id:
        student.objects.create(name=name,email=email,age=age,image=image)
        return render(request,"home.html",{"success":"Done You are registered succesfully!"})
    else:
        st=student.objects.get(pk=id)
        st.name=name
        st.email=email
        st.age=age
        st.save()
        return render(request,"home.html",{"success":"Done Your Details are updated!"})


def display(request):
    students= student.objects.all()
    return render(request,"display.html",{"students":students})

def delete_student(request):
    id= request.GET.get('id')
    st= student.objects.get(pk=id)
    st.delete()
    return redirect("display")

def edit_student(request):
    id= request.GET.get('id')
    st= student.objects.get(pk=id)
    if request.FILES:
        st.image=request.FILES.get('image')
        st.save()
        return render(request,"home.html",{"st":st})
    else:
        return render(request,"home.html",{"st":st})


