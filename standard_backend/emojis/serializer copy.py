from rest_framework import serializers
from .models import Emojis

class EmojiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emojis,
        fields = ['id', 'name', 'icon']