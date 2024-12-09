from django.contrib import admin
from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('create-joke/', JokeCreateAPIView.as_view()),  # POST
    path('list-jokes/', ListJokes.as_view()),  # GET
    path('retrieve/<int:pk>/', JokeRetrieveAPIView.as_view()),  # GET, DELETE
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    # /users/
    # /users/me/
    # /users/set_username/
    # /users/reset_username/
    # /users/reset_username_confirm/
    # /token/login/
    # /token/logout/

    # 1) POST: api/auth/token/login/
    # username=<username>
    # password=<password>
    # Получение токена...
    # 2) GET: api/auth/users/me/
    # Headers:
    # Authorization: Token <token>
]
