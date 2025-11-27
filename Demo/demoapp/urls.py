from django.urls import path
from demoapp.views import *
urlpatterns=[
    path("",Home,name="Home"),
    path("Name",Name,name="Name"),
    path("Email",Email,name="Email")
]