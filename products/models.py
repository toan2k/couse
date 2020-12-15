from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(default="", max_length=255)
    slug = models.CharField(default="", max_length=100)
    description = models.TextField(default="")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    teaching = models.CharField(default="", max_length=255)
    image_teacher = models.ImageField(default=None, upload_to='static/media/teacher')
    slug = models.CharField(default="", max_length=100)
    description = models.TextField(default="")
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.teaching
    

class Course(models.Model):
    title = models.CharField(default="", max_length=255)
    slug = models.CharField(default="", max_length=100)
    image_course = models.ImageField(default=None, upload_to='static/media/course')
    description = models.TextField(default="")
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title


class Variation(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(default="", max_length=255)
    price = models.FloatField(default=0)
    sale_price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title

# class Rating(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
#     rate = models.IntegerField(default=0)
#     comment = models.TextField(default = "")

# class Comment(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
#     rate = models.IntegerField(default=0)
#     comment = models.TextField(default = "")