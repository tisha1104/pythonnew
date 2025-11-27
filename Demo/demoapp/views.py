from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,"Home.html")
def Name(request):
    return render(request,"Name.html")
def Email(request):
    return render(request,"Email.html")