from django.db import models
from accounts.models import CustomerUser

# Create your models here.

class CategoryEvent(models.Model):
    title = models.CharField(default="", max_length=255)
    slug = models.CharField(default="", max_length=100)
    description = models.TextField(default="")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Events(models.Model):
    title = models.CharField(default="", max_length=255)
    slug = models.CharField(default="", max_length=100)
    image_course = models.ImageField(default=None, upload_to='static/media/event')
    content = models.TextField(default="")
    category = models.ForeignKey(CategoryEvent, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title


class CommentEvent(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    comment = models.TextField(default = "")
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.comment
