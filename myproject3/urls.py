from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URLs
    path('api/', include('myapp.urls')),  # Include API endpoints and custom views
]
