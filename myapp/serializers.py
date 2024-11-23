from rest_framework import serializers
from .models import *

class AgriculturalOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgriculturalOfficer
        fields = '__all__'

class AuthGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthGroup
        fields = '__all__'

class AuthGroupPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthGroupPermissions
        fields = '__all__'

class AuthPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthPermission
        fields = '__all__'

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'

class AuthUserGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUserGroups
        fields = '__all__'

class AuthUserUserPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUserUserPermissions
        fields = '__all__'

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'

class BatchPurchaseRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatchPurchaseRequest
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class CustomerReqVisitToFarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerReqVisitToFarmer
        fields = '__all__'

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'

class DistributorCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = DistributorCompany
        fields = '__all__'

class DistributorCompanyDemandForProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistributorCompanyDemandForProduct
        fields = '__all__'

class DjangoAdminLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoAdminLog
        fields = '__all__'

class DjangoContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoContentType
        fields = '__all__'

class DjangoMigrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoMigrations
        fields = '__all__'

class DjangoSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoSession
        fields = '__all__'

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'

class FarmerSeedDemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerSeedDemand
        fields = '__all__'

class FarmerSeedStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerSeedStock
        fields = '__all__'

class FinancialsupportCustomerToFarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialsupportCustomerToFarmer
        fields = '__all__'

class HarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harvest
        fields = '__all__'

class HarvestFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HarvestFields
        fields = '__all__'

class HarvestFieldsCropsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HarvestFieldsCropsType
        fields = '__all__'

class HarvestFieldsSoilTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HarvestFieldsSoilType
        fields = '__all__'

class HarvestHarvestFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HarvestHarvestFields
        fields = '__all__'

class LiveTemperatureHumidityMonitoringOfProductBatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveTemperatureHumidityMonitoringOfProductBatches
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'

class Loan20Serializer(serializers.ModelSerializer):
    class Meta:
        model = Loan20
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class MarketPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketPlace
        fields = '__all__'

class MarketPlaceProductSoldSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketPlaceProductSold
        fields = '__all__'

class NutritionistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutritionists
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class PurchaseRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseRequest
        fields = '__all__'

class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = '__all__'

class SampleResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleResult
        fields = '__all__'

class SeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seed
        fields = '__all__'

class SeedStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeedStock
        fields = '__all__'

class SeedStock20Serializer(serializers.ModelSerializer):
    class Meta:
        model = SeedStock20
        fields = '__all__'

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class WirehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wirehouse
        fields = '__all__'

class WirehouseManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WirehouseManager
        fields = '__all__'
