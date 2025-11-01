from .models import AirQualityRecord
import django_filters as filters

class AirQualityRecordFilter(filters.FilterSet):
    start_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = AirQualityRecord
        fields = ['start_date', 'end_date']