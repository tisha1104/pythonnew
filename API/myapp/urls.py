from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("addproduct/",addproduct,name="addproduct"),
    path('get_products/', get_products, name='get_products'), 
    path('products/update/<id>/', update_student, name='update_student'),
]


urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)