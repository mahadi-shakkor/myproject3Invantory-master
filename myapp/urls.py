from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, UserViewSet
from django.urls import path
from . import views

# Set up the DRF router
router = DefaultRouter()
router.register(r'locations', LocationViewSet, basename='location')
router.register(r'users', UserViewSet)

# Combine router-generated URLs with custom ones
urlpatterns = router.urls + [
    path('users/list/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
]
