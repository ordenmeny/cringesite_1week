from django.urls import path, include
from .views import *

urlpatterns = [
    path('signup/', RegisterUserView.as_view(), name='signup'),
    path('login/', LoginUser.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
]