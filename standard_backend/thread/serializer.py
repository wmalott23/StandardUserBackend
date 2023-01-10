from rest_framework import serializers
from .models import Thread

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ['id', 'subject', 'subject_id', 'title', 'description', 'user_info', 'user_info_id', 'view', 'timestamp']
        depth = 1
    subject_id = serializers.IntegerField(write_only=True)
    user_info_id = serializers.IntegerField(write_only=True)