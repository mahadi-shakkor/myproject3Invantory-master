from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, UserViewSet

router = DefaultRouter()
router.register(r'locations', LocationViewSet, basename='location')  # Register the LocationViewSet
router.register(r'users', UserViewSet)  # Register the UserViewSet

urlpatterns = router.urls  # Generate URLs from the router
