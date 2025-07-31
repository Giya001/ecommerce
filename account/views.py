from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import response
from rest_framework.decorators import api_view

from account.serializers import UserSerializer


# Create your views here.
@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return response.Response(serializer.data)