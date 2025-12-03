from django.contrib import admin
from demoapp.models import *
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','age')
    search_fields=('first_name','last_name','email','age')


    admin.site.register(student)
    admin.site.register(course)
