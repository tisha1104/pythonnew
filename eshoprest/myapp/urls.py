from django.urls import path,include
from myapp.views import *
from rest_framework import routers

router=routers.DefaultRouter()
router.register("users",UserViewSet)
router.register("categories",CategoryViewSet)
router.register("products",ProductViewSet)

urlpatterns=[
    path('',include(router.urls))
]