from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path("",home,name="home"),
    path("edit",edit_product,name="edit"),
    path("delete",delete_product,name="delete"),
    path("registration",user_registration,name="registration"),
    path('login',user_login,name="login"),
    path('logout',user_logout,name="logout")
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)