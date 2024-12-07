from rest_framework import serializers
from .models import *


class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JokeModel
        fields = ("topic_input", "text_joke")

