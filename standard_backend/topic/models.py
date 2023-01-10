from django.db import models

# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)