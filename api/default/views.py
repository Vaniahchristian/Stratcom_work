from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . serilaisers import *
from django.contrib.auth.models import User

# Create your views here.
@api_view(['GET'])
def homeView(request):
    message = {
        "message":"welcome to our API endpoints"
    }
    return Response(message, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def peopleView(request):
    if request.method == 'GET':
        all_users = User.objects.all()
        serialiser = UserSerialiser(all_users, many = True)
        return Response(serialiser.data, status=status.HTTP_200_OK)
    else:
        data = request.data
        serialiser = UserSerialiser(data = data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def peopleDetailsView(request, **kwargs):
    try:
        user = User.objects.get(pk = kwargs['id'])
    except User.DoesNotExist as e:
        return Response({"details":f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serialiser = UserSerialiser(user)
        return Response(serialiser.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        data = request.data
        serialiser = UserSerialiser(data=data, partial = True)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_202_ACCEPTED)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        username = user.username
        msg = f"user {username} deleted successfully!"
        user.delete()
        return Response({"message":msg}, status=status.HTTP_404_NOT_FOUND)