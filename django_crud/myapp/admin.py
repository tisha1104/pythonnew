from django.contrib import admin
from myapp.models import *
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display =('name','age','email')

admin.site.register(student,StudentAdmin) 
