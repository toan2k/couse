from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.


class CustomerUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=250)
    image_user = models.ImageField(default=None, upload_to='static/media/customeruser')

class UserType(models.Model):
    title = models.CharField(default="", max_length=255)
    CustomerUser = models.ForeignKey( CustomerUser,on_delete=models.CASCADE)