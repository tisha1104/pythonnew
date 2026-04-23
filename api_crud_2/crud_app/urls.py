from django.urls import path
from crud_app.views import *

urlpatterns=[
    path("view/",view_student,name="view"),
    path("add/",add_student,name="add"),
    path("viewbyid/<id>",view_byid,name="viewbyid"),
    path("update/<id>",udate_student,name="update"),
    path("delete/<id>",delete_student,name="delete")
]