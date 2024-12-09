from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JokeModel
        fields = ("topic_input", "text_joke")


# class UserCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("username", "")