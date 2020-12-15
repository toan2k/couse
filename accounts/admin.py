from django.contrib import admin
from .models import CustomerUser, UserType
# Register your models here.

admin.site.register(UserType)
admin.site.register(CustomerUser)
