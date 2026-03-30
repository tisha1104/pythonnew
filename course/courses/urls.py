from django.urls import path
from .views import *

urlpatterns=[
    path('', course_list, name='course_list'),
    path('create/', create_course, name='create_course'),
    path('home',home,name="home"),
    path('<int:id>/', course_detail, name='course_detail'),
]