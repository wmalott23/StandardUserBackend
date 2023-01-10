from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserInfoSerializer
from .models import UserInfo

# Create your views here.

@api_view(['GET', 'POST'])
def user_info_list(request):
    if request.method == 'GET':
        users = UserInfo.objects.all()
        serializer = UserInfoSerializer(users, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def user_info_detail(request, pk):
    user = get_object_or_404(UserInfo, pk=pk)
    if request.method == 'GET':
        serializer = UserInfoSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserInfoSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)