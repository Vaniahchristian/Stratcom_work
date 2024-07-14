from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from .serializers import *
from django.contrib.auth.models import User

# Create your views here.


@api_view(['GET'])
def homeView(request):
    message = {

       "message" : "welcome to our api endpoints"

    }
    return Response(message,status=status.HTTP_200_OK)


@api_view(['GET'])
def peopleView(request):
    if request.method =='GET':
        all_users = User.objects.all()
        serializer = UserSerialiser(all_users,many = True)
    
    return response(serialiser.data, status=status.HTTP_200_OK)
    else:
        data = request.data
        serialiser = UserSerialiser(data = data)
