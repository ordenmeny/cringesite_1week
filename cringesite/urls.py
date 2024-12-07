from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("users.urls")),
    path('api/', include("api_app.urls")),
    path('', include("main_app.urls")),
]
