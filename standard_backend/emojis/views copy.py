from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import EmojiSerializer
from .models import Emojis

# Create your views here.

@api_view(['GET', 'POST'])
def emoji_list(request):
    if request.method == 'GET':
        emojis = Emojis.objects.all()
        serializers = EmojiSerializer(emojis, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = EmojiSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def emoji_detail(request, pk):
    emoji = get_object_or_404(Emojis, pk=pk)
    if request.method == 'GET':
        serializer = EmojiSerializer(emoji)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EmojiSerializer(emoji, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        emoji.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)