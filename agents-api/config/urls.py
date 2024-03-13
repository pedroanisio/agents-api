# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('prompt.urls')),  # Adjust 'prompt' to your app's name
]
