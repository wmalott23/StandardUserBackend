from rest_framework import serializers
from .models import CommentEmoji

class CommentEmojiSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentEmoji
        fields = ['id', 'comment', 'comment_id', 'emoji', 'emoji_id', 'user_info', 'user_info_id']
        depth = 1
        comment_id = serializers.IntegerField(write_only=True)
        emoji_id = serializers.IntegerField(write_only=True)
        user_info_id = serializers.IntegerField(write_only=True)