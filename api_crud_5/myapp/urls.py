from django.urls import path,include
from myapp.views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r"product",ProductViewset)

urlpatterns = router.urls