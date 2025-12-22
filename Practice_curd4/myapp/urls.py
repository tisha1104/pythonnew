from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns= [
    path('index',index,name="index"),
    path("delete",delete_student,name="delete"),
    path("edit",edit_student,name="edit"),
    path("registration",student_registration,name="registration"),
    path('',student_login,name="login"),
    path('logout',user_logout,name="logout")
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)