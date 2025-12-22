from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path("",home,name="home"),
    path("register",register,name="register"),
    path("display",display,name="display"),
    path("delete",delete_student,name="delete"),
    path("edit",edit_student,name="edit")
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)