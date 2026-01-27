from django.urls import path
from curdapp.views import *

urlpatterns=[
    path("view",view_student,name="view"),
    path("add",add_student,name="add"),
    path("viewbyid/<id>",view_byid,name="viewbyid"),
    path("update/<id>",update_student,name="update"),
    path("delete/<id>",delete_student,name="delete")

]