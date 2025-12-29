from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("",home,name="home"),
    path("edit",edit_product,name="edit"),
    path("delete",delete_product,name="delete"),
    path("ragistation",ragistation,name="ragistation"),
    path("login",login_data,name="login"),
    path('logout',logout_data,name="logout")
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)