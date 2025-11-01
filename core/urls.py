from .views import AirQualityRecordViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'air_quality_records', AirQualityRecordViewSet, basename='air_quality_record')

urlpatterns = [
    path('', include(router.urls)),
]
