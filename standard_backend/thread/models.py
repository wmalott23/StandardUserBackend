from django.db import models
from subject.models import Subject
from user.models import UserInfo

# Create your models here.

class Thread(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=(100))
    description = models.CharField(max_length=(255))
    user_info = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    view = models.CharField(max_length=(30))
    timestamp = models.DateField()
