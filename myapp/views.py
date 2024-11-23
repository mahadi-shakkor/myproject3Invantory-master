from rest_framework import viewsets
from .models import *
from .serializers import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

class SignupAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not username or not password:
            raise ValidationError("Username and password are required.")
        
        if User.objects.filter(username=username).exists():
            raise ValidationError("A user with this username already exists.")
        
        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)

from django.shortcuts import render

def signup_page(request):
    return render(request, 'signup.html')


@api_view(['GET'])
def sample_api(request):
    return Response({'message': 'Hello from Django!'})

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]  # No authentication required for login

    def post(self, request, *args, **kwargs):
        userid = request.data.get('userid')
        password = request.data.get('password')

        if not userid or not password:
            return Response({'error': 'User ID and Password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=userid, password=password)
        if user:
            login(request, user)  # Log the user in
            return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home_view(request):
    return render(request, 'home.html')

from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AgriculturalOfficerViewSet(viewsets.ModelViewSet):
    queryset = AgriculturalOfficer.objects.all()
    serializer_class = AgriculturalOfficerSerializer

class AuthGroupViewSet(viewsets.ModelViewSet):
    queryset = AuthGroup.objects.all()
    serializer_class = AuthGroupSerializer

class AuthGroupPermissionsViewSet(viewsets.ModelViewSet):
    queryset = AuthGroupPermissions.objects.all()
    serializer_class = AuthGroupPermissionsSerializer

class AuthPermissionViewSet(viewsets.ModelViewSet):
    queryset = AuthPermission.objects.all()
    serializer_class = AuthPermissionSerializer

class AuthUserViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer

class AuthUserGroupsViewSet(viewsets.ModelViewSet):
    queryset = AuthUserGroups.objects.all()
    serializer_class = AuthUserGroupsSerializer

class AuthUserUserPermissionsViewSet(viewsets.ModelViewSet):
    queryset = AuthUserUserPermissions.objects.all()
    serializer_class = AuthUserUserPermissionsSerializer

class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

class BatchPurchaseRequestViewSet(viewsets.ModelViewSet):
    queryset = BatchPurchaseRequest.objects.all()
    serializer_class = BatchPurchaseRequestSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerReqVisitToFarmerViewSet(viewsets.ModelViewSet):
    queryset = CustomerReqVisitToFarmer.objects.all()
    serializer_class = CustomerReqVisitToFarmerSerializer

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class DistributorCompanyViewSet(viewsets.ModelViewSet):
    queryset = DistributorCompany.objects.all()
    serializer_class = DistributorCompanySerializer

class DistributorCompanyDemandForProductViewSet(viewsets.ModelViewSet):
    queryset = DistributorCompanyDemandForProduct.objects.all()
    serializer_class = DistributorCompanyDemandForProductSerializer

class DjangoAdminLogViewSet(viewsets.ModelViewSet):
    queryset = DjangoAdminLog.objects.all()
    serializer_class = DjangoAdminLogSerializer

class DjangoContentTypeViewSet(viewsets.ModelViewSet):
    queryset = DjangoContentType.objects.all()
    serializer_class = DjangoContentTypeSerializer

class DjangoMigrationsViewSet(viewsets.ModelViewSet):
    queryset = DjangoMigrations.objects.all()
    serializer_class = DjangoMigrationsSerializer

class DjangoSessionViewSet(viewsets.ModelViewSet):
    queryset = DjangoSession.objects.all()
    serializer_class = DjangoSessionSerializer

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class FarmerSeedDemandViewSet(viewsets.ModelViewSet):
    queryset = FarmerSeedDemand.objects.all()
    serializer_class = FarmerSeedDemandSerializer

class FarmerSeedStockViewSet(viewsets.ModelViewSet):
    queryset = FarmerSeedStock.objects.all()
    serializer_class = FarmerSeedStockSerializer

class FinancialsupportCustomerToFarmerViewSet(viewsets.ModelViewSet):
    queryset = FinancialsupportCustomerToFarmer.objects.all()
    serializer_class = FinancialsupportCustomerToFarmerSerializer

class HarvestViewSet(viewsets.ModelViewSet):
    queryset = Harvest.objects.all()
    serializer_class = HarvestSerializer

class HarvestFieldsViewSet(viewsets.ModelViewSet):
    queryset = HarvestFields.objects.all()
    serializer_class = HarvestFieldsSerializer

class HarvestFieldsCropsTypeViewSet(viewsets.ModelViewSet):
    queryset = HarvestFieldsCropsType.objects.all()
    serializer_class = HarvestFieldsCropsTypeSerializer

class HarvestFieldsSoilTypeViewSet(viewsets.ModelViewSet):
    queryset = HarvestFieldsSoilType.objects.all()
    serializer_class = HarvestFieldsSoilTypeSerializer

class HarvestHarvestFieldsViewSet(viewsets.ModelViewSet):
    queryset = HarvestHarvestFields.objects.all()
    serializer_class = HarvestHarvestFieldsSerializer

class LiveTemperatureHumidityMonitoringOfProductBatchesViewSet(viewsets.ModelViewSet):
    queryset = LiveTemperatureHumidityMonitoringOfProductBatches.objects.all()
    serializer_class = LiveTemperatureHumidityMonitoringOfProductBatchesSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class Loan20ViewSet(viewsets.ModelViewSet):
    queryset = Loan20.objects.all()
    serializer_class = Loan20Serializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class MarketPlaceViewSet(viewsets.ModelViewSet):
    queryset = MarketPlace.objects.all()
    serializer_class = MarketPlaceSerializer

class MarketPlaceProductSoldViewSet(viewsets.ModelViewSet):
    queryset = MarketPlaceProductSold.objects.all()
    serializer_class = MarketPlaceProductSoldSerializer

class NutritionistsViewSet(viewsets.ModelViewSet):
    queryset = Nutritionists.objects.all()
    serializer_class = NutritionistsSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PurchaseRequestViewSet(viewsets.ModelViewSet):
    queryset = PurchaseRequest.objects.all()
    serializer_class = PurchaseRequestSerializer

class RetailerViewSet(viewsets.ModelViewSet):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer

class SampleResultViewSet(viewsets.ModelViewSet):
    queryset = SampleResult.objects.all()
    serializer_class = SampleResultSerializer

class SeedViewSet(viewsets.ModelViewSet):
    queryset = Seed.objects.all()
    serializer_class = SeedSerializer

class SeedStockViewSet(viewsets.ModelViewSet):
    queryset = SeedStock.objects.all()
    serializer_class = SeedStockSerializer

class SeedStock20ViewSet(viewsets.ModelViewSet):
    queryset = SeedStock20.objects.all()
    serializer_class = SeedStock20Serializer

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class WirehouseViewSet(viewsets.ModelViewSet):
    queryset = Wirehouse.objects.all()
    serializer_class = WirehouseSerializer

class WirehouseManagerViewSet(viewsets.ModelViewSet):
    queryset = WirehouseManager.objects.all()
    serializer_class = WirehouseManagerSerializer
