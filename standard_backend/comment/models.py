from django.db import models
from thread.models import Thread
from user.models import UserInfo

# Create your models here.

class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    timestamp = models.DateField()
    message = models.CharField(max_length=(255))
    user_info = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    