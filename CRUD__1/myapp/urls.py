from django.urls import path
from myapp.views import *

urlpatterns=[
    path("home",home,name="home"),
    path("delete",delete_student,name="delete"),
    path("edit",edit_student,name="edit"),
    path("",registration_user,name="registration"),
    path("login",user_login,name="login"),
    path("logout",user_logout,name="logout")
]