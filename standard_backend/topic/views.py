from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import TopicSerializer
from .models import Topic

# Create your views here.

@api_view(['GET', 'POST'])
def topic_list(request):
    if request.method == 'GET':
        topic = Topic.objects.all()
        serializer = TopicSerializer(topic, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TopicSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def topic_detail(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    if request.method == 'GET':
        serializer = TopicSerializer(topic)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TopicSerializer(topic, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)