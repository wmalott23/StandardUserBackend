from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    icon = models.CharField(max_length=255)