from django.urls import path,include
from myapp.views import *
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


router=DefaultRouter()
router.register("product",Productviewset)

urlpatterns=[
    path("",include(router.urls))
]

