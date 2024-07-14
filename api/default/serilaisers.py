from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = "__all__"
        fields = ['id', 'username', 'first_name', 'last_name', 'email']