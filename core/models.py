from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Device(models.Model):

    url = models.CharField(max_length=200)

    access_token = models.CharField(max_length=1000, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
