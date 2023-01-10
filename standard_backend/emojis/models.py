from django.db import models

# Create your models here.

class Emojis(models.Model):
    name = models.CharField(max_length=(30))
    icon = models.CharField(max_length=(255))