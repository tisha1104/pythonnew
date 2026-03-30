from django.urls import path
from .views import *

urlpatterns = [
    path('<int:course_id>/', enroll_course, name='enroll_course'),
    path('dashboard/', student_dashboard, name='dashboard'),
]