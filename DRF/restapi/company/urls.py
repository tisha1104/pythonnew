from django.urls import path
from company.views import *

urlpatterns=[
    path("depts",DeptApi.as_view()),
    path("depts/<id>",DeptupdateAPI.as_view()),
    path("emps/dept/<int:id>/", addEmp, name="addEmp"),
    path("emps",getemps,name="emps"),
    path("emps/dept/<id>/<eid>",updateEmp,name="updateemp"),
    path("emps/<id>",EmpById.as_view())

]