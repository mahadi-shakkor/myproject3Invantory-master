from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework.permissions import IsAuthenticated

router = DefaultRouter()
router.register(r'agricultural-officer', AgriculturalOfficerViewSet)
router.register(r'auth-group', AuthGroupViewSet)
router.register(r'auth-group-permissions', AuthGroupPermissionsViewSet)
router.register(r'auth-permission', AuthPermissionViewSet)
router.register(r'auth-user', AuthUserViewSet)
router.register(r'auth-user-groups', AuthUserGroupsViewSet)
router.register(r'auth-user-user-permissions', AuthUserUserPermissionsViewSet)
router.register(r'batch', BatchViewSet)
router.register(r'batch-purchase-request', BatchPurchaseRequestViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'customer-req-visit-to-farmer', CustomerReqVisitToFarmerViewSet)
router.register(r'delivery', DeliveryViewSet)
router.register(r'distributor-company', DistributorCompanyViewSet)
router.register(r'distributor-company-demand-for-product', DistributorCompanyDemandForProductViewSet)
router.register(r'django-admin-log', DjangoAdminLogViewSet)
router.register(r'django-content-type', DjangoContentTypeViewSet)
router.register(r'django-migrations', DjangoMigrationsViewSet)
router.register(r'django-session', DjangoSessionViewSet)
router.register(r'farmer', FarmerViewSet)
router.register(r'farmer-seed-demand', FarmerSeedDemandViewSet)
router.register(r'farmer-seed-stock', FarmerSeedStockViewSet)
router.register(r'financialsupport-customer-to-farmer', FinancialsupportCustomerToFarmerViewSet)
router.register(r'harvest', HarvestViewSet)
router.register(r'harvest-fields', HarvestFieldsViewSet)
router.register(r'harvest-fields-crops-type', HarvestFieldsCropsTypeViewSet)
router.register(r'harvest-fields-soil-type', HarvestFieldsSoilTypeViewSet)
router.register(r'harvest-harvest-fields', HarvestHarvestFieldsViewSet)
router.register(r'live-temperature-humidity-monitoring', LiveTemperatureHumidityMonitoringOfProductBatchesViewSet)
router.register(r'loan', LoanViewSet)
router.register(r'loan20', Loan20ViewSet)
router.register(r'location', LocationViewSet)
router.register(r'marketplace', MarketPlaceViewSet)
router.register(r'marketplace-product-sold', MarketPlaceProductSoldViewSet)
router.register(r'nutritionists', NutritionistsViewSet)
router.register(r'product', ProductViewSet)
router.register(r'purchase-request', PurchaseRequestViewSet)
router.register(r'retailer', RetailerViewSet)
router.register(r'sample-result', SampleResultViewSet)
router.register(r'seed', SeedViewSet)
router.register(r'seed-stock', SeedStockViewSet)
router.register(r'seed-stock20', SeedStock20ViewSet)
router.register(r'sensor', SensorViewSet)
router.register(r'supplier', SupplierViewSet)
router.register(r'users', UserViewSet)
router.register(r'wirehouse', WirehouseViewSet)
router.register(r'wirehouse-manager', WirehouseManagerViewSet)
from django.urls import path
from .views import sample_api

from django.views.generic import TemplateView

from django.urls import path
from .views import UserLoginAPIView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', TemplateView.as_view(template_name='signup.html'), name='signup'),  # Add this line
     
    path('api/signup/', SignupAPIView.as_view(), name='api-signup'),
    path('api/', include(router.urls)),
    path('api/login/', UserLoginAPIView.as_view(), name='api-login'),
    path('home/', home_view, name='home'),
    path('api/sample/', sample_api),
]






class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
