from django.urls import path
from myapp.views import *
urlpatterns=[
    path('',index,name='index'),
    path('jewellery/',jewellery,name='jewellery'),
    path('fashion/',fashion,name='fashion'),
    path('electronic/',electronic,name='electronic')
]