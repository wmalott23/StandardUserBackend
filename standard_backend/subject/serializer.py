from rest_framework import serializers
from .models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'topic', 'topic_id', 'description', 'user', 'user_info_id', 'timestamp']
        depth = 1
        topic_id = serializers.IntegerField(write_only=True)
        user_info_id = serializers.IntegerField(write_only=True)