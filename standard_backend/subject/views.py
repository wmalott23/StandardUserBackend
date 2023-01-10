from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import SubjectSerializer
from .models import Subject

# Create your views here.

@api_view(['GET', 'POST'])
def subject_list(request):
    if request.method == 'GET':
        subjects = Subject.objects.all()
        serializers = SubjectSerializer(subjects, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = SubjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'GET':
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SubjectSerializer(subject, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)