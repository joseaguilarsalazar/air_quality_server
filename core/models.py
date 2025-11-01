from django.db import models

# Create your models here.

class AirQualityRecord(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    mhz19 = models.FloatField()
    mq2 = models.FloatField()
    mq7 = models.FloatField()
    mq135 = models.FloatField()
    dht22_temp = models.FloatField()
    dht22_humidity = models.FloatField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)