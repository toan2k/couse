from django.contrib import admin
from .models import CategoryEvent, Events, CommentEvent
# Register your models here.

admin.site.register(CategoryEvent)
admin.site.register(Events)
admin.site.register(CommentEvent)