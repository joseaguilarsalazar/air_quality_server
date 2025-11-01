from .models import AirQualityRecord
from rest_framework.serializers import ModelSerializer

class AirQualityRecordSerializer(ModelSerializer):
    class Meta:
        model = AirQualityRecord
        fields = '__all__'