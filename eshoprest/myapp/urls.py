from django.urls import path,include
from myapp.views import *
from rest_framework import routers

router=routers.DefaultRouter()
router.register("users",UserViewSet)
router.register("categories",CategoryViewSet)
router.register("products",ProductViewSet)
router.register("address",AddressViewset,basename="address")
router.register("carts",CartViewSet,basename="carts")

urlpatterns=[
    path('',include(router.urls)),
    path("payment",payment,name="payment"),
    path("order/create",create_order,name="orders")
]