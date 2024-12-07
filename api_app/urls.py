from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('create-joke/', JokeCreateAPIView.as_view()),
    # path('detail/<int:pk>/', JokeDetailAPIView.as_view()),
]