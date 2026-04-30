from django.urls import path
from myapp.views import *

urlpatterns=[
    path("",home,name="home"),
    path("delete",delete_student,name="delete"),
    path("edit",edit_student,name="edit")
]