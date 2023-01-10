from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import CommentEmojiSerializer
from .models import CommentEmoji

# Create your views here.

@api_view(['GET', 'POST'])
def comment_emoji_list(request):
    if request.method == 'GET':
        comment_emojis = CommentEmoji.objects.all()
        serializers = CommentEmojiSerializer(comment_emojis, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = CommentEmojiSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def comment_emoji_detail(request, pk):
    comment_emoji = get_object_or_404(CommentEmoji, pk=pk)
    if request.method == 'GET':
        serializer = CommentEmojiSerializer(comment_emoji)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommentEmojiSerializer(comment_emoji, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        comment_emoji.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)