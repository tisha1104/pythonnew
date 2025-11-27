from django.urls import path
from myapp.views import*
urlpatterns=[
    path("",index,name="index"),
    path("About",About,name="About"),
    path("Contact",contact,name="Contact"),
    path("Help",help,name="Help")
]