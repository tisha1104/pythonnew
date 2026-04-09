from django.contrib import admin
from crudapp.models import *
from crudapp.models import Categories
# Register your models here.
admin.site.register(Product)
admin.site.register(Categories)