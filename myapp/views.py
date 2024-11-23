from rest_framework.viewsets import ModelViewSet
from .models import Location, User
from .serializers import LocationSerializer, UserSerializer

# Define LocationViewSet
class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# Define UserViewSet
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Define custom views
from django.shortcuts import render
import requests

def user_list(request):
    response = requests.get('http://127.0.0.1:8000/api/users/')
    users = response.json()
    return render(request, 'user_list.html', {'users': users})

def user_create(request):
    return render(request, 'user_form.html')
