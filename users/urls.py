from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('signup/', RegisterUserView.as_view(), name='signup'),
    path('login/', LoginUser.as_view(), name='signup'),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('', include('django.contrib.auth.urls')),
]
    # url-prefix: api-auth/
    # 1) Авторизация:
    # POST: /auth/token/login/
    # username=<username>
    # password=<password>
    # Получение токена (его нужно сохранить на клиенте)

    # 2) Создание нового пользователя:
    # username=<username>
    # password=<password>
    # POST: /auth/users/

    # 3) Получение всех пользователей:
    # GET: /auth/users/
    # Headers: Authorization: Token <token>

    # 4) Получение текущего пользователя:
    # GET: /auth/users/me/
    # Headers: Authorization: Token <token>

    # 5) /auth/token/logout/
