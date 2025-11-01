from rest_framework.viewsets import ModelViewSet
from .models import AirQualityRecord
from .serializer import AirQualityRecordSerializer
from rest_framework.permissions import AllowAny
from .filters import AirQualityRecordFilter
from django_filters.rest_framework import DjangoFilterBackend


class AirQualityRecordViewSet(ModelViewSet):
    queryset = AirQualityRecord.objects.all().order_by('-timestamp')
    serializer_class = AirQualityRecordSerializer
    filterset_class = AirQualityRecordFilter
    filter_backends = [DjangoFilterBackend]
    permission_classes = [AllowAny]
