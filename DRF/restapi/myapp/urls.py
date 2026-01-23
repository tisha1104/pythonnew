from django.urls import path
from myapp.views import *

urlpatterns=[
    path('get_api/', get_api, name='get_api'),
    path('post_api/', post_api, name='post_api'),
    path('put_api/', put_api, name='put_api'),
    path('delete_api/', delete_api, name='delete_api'),
]