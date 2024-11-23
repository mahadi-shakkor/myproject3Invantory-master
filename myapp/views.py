from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
import requests
from .models import Location, User
from .serializers import LocationSerializer, UserSerializer

# API ViewSets
class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Custom views for templates
def user_list(request):
    """
    Fetch data from API and render it in the template.
    """
    try:
        # Fetch data from the API
        response = requests.get('http://127.0.0.1:8000/api/users/')
        response.raise_for_status()  # Raise exception for HTTP errors
        users = response.json()  # Parse the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        users = []  # Set users to an empty list if the API call fails

    return render(request, 'user_list.html', {'users': users})

def user_create(request):
    """
    Render a form for creating a new user.
    """
    return render(request, 'user_form.html')


from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

def user_create(request):
    """
    Render a form for creating a new user and handle the form submission.
    """
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            return redirect('user_list')  # Redirect to the user list page
    else:
        form = UserForm()

    return render(request, 'user_form.html', {'form': form})


from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


from django.shortcuts import render
import requests

def user_list(request):
    """
    Fetch data from the DRF API and render it in a template.
    """
    try:
        response = requests.get('http://127.0.0.1:8000/api/users/')  # API URL
        response.raise_for_status()
        users = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        users = []

    return render(request, 'user_list.html', {'users': users})
