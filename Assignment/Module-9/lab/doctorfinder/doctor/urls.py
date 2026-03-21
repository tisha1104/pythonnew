from django.urls import path
from doctor import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home),
    path('doctors/', views.doctor_list),
    path('contact/', views.contact),
    path('login/', auth_views.LoginView.as_view(), name='login'),   
]