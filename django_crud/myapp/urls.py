from django.urls import path
from myapp.views import *

urlpatterns=[
    path('',home,name='home'),
    path('display',display,name='display'),
    path('registraion',registraion_student,name='registraion'),
    path('delete',delete_student,name='delete'),
    path('edit',edit_student,name='edit')
]