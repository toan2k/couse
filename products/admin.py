from django.contrib import admin

# Register your models here.
from .models import Category, Course, Teacher, Variation

# Register your models here.
admin.site.register(Category)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Variation)
