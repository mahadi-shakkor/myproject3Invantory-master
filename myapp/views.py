from rest_framework.viewsets import ModelViewSet
from .models import Location,User
from .serializers import LocationSerializer,UserSerializer

class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

