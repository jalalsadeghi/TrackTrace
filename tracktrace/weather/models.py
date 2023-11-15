from django.db import models
from tracktrace.common.models import BaseModel


# Create your models here.
class Weather(BaseModel):
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    temperature = models.FloatField()
    wind_speed = models.FloatField()
    zipcode = models.IntegerField()

    def __str__(self):
        return f"{self.city}, {self.country}"