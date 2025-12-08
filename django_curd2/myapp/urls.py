from django.urls import path
from myapp.views import *

urlpatterns=[
    path("",home,name="home"),
    path("delete",delete_product,name="delete"),
    path("edit",edit_product,name="edit")
]