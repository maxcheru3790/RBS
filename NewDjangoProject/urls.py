# project/urls.py (main project's urls.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site path defined here
    path('', include('myapp.urls')),  # Include app URLs for the root path
]
