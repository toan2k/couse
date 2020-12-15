from django.contrib import admin
from .models import CategoryQuiz, EventQuiz, Quiz

# Register your models here.

admin.site.register(CategoryQuiz)
admin.site.register(EventQuiz)
admin.site.register(Quiz)
