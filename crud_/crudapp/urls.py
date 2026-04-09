from django.urls import *
from crudapp.views import *
from django.conf import settings
from django.conf.urls import static

urlpatterns=[
    path("",home,name="home")
]

# urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)