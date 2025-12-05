from django.shortcuts import render,redirect
from myapp.models import student
# Create your views here.
def home(request):
    return render(request, 'home.html')

def registraion_student(request):
    id = request.POST.get('id') 
    name = request.POST.get('name')
    email = request.POST.get('email')
    age = request.POST.get('age')

    if not id :
        student.objects.create(name=name,email=email,age=age)
        return render(request,'home.html',{'success':'student ragistraion succesfully'})
    else:
        st=student.objects.get(pk=id)
        st.name=name
        st.email=email
        st.age=age
        st.save()
        return render(request,'home.html',{'success':'student ragistraion succesfully'})
    

def display(request):
    students=student.objects.all()
    return render(request,'display.html',{'student':students})

def delete_student(request):
    id=request.GET.get("id")
    st=student.objects.get(pk=id)
    st.delete()
    return redirect("display")
    
def edit_student(request):

    id=request.GET.get("id")
    st=student.objects.get(pk=id)
    return render(request,"home.html",{"st":st})


