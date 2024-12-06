from django.urls import path, include
from .views import *

app_name = "main_app"

urlpatterns = [
    path('', HomePage.as_view(), name="home_page"),
]