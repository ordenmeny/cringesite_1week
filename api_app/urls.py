from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('create-joke/', JokeCreateAPIView.as_view()),  # POST
    path('list-jokes/', ListJokes.as_view()),  # GET
    path('retrieve/<int:pk>/', JokeRetrieveAPIView.as_view()),  # GET, DELETE
]
