from django.db import models
from accounts.models import CustomerUser

# Create your models here.

class CategoryQuiz(models.Model):
    title = models.CharField(default="", max_length=255)
    slug = models.CharField(default="", max_length=100)
    description = models.TextField(default="")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class EventQuiz(models.Model):
    title = models.CharField(default="", max_length=255)
    slug = models.CharField(default="", max_length=100)
    image_eventqz = models.ImageField(default=None, upload_to='static/media/eventqz')
    description = models.TextField(default="")
    category = models.ForeignKey(CategoryQuiz, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Quiz(models.Model):
    title = models.CharField(default="", max_length=255)
    slug = models.CharField(default="", max_length=100)
    image_qz = models.ImageField(default=None, upload_to='static/media/eventqz')
    question = models.CharField(default="", max_length=255)
    solution = models.CharField(default="", max_length=255)
    event = models.ForeignKey(EventQuiz, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title


