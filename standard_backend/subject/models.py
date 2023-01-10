from django.db import models
from topic.models import Topic
from user.models import UserInfo

# Create your models here.

class Subject(models.Model):
    title = models.CharField(max_length=(30))
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    description = models.CharField(max_length=(255))
    user_info = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
