from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.


def home(request):
    student=Student.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        emial=request.POST['emial']
        sub=request.POST['sub']
        image=request.FILES['image']
        Student.objects.create(name=name,emial=emial,sub=sub,image=image)
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
        s=Student.objects.get(pk=id)
        s.name=name
        s.emial=emial
        s.sub=sub
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