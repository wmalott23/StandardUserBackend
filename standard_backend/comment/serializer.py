from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment,
        fields = ['id', 'thread', 'thread_id', 'timestamp', 'message', 'user_info', 'user_info_id']
        depth = 1
        thread_id = serializers.IntegerField(write_only=True)
        user_info_id = serializers.IntegerField(write_only=True)