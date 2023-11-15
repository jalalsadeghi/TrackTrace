from django.db import models

from tracktrace.common.models import BaseModel
from tracktrace.weather.models import Weather


class Shipments(BaseModel):
    class CarrierTypeChoice(models.TextChoices):
        DHL = 'DHL'
        DPD = 'DPD'
        FedEx = 'FedEx'
        GLS = 'GLS'
        UPS = 'UPS'

    class StatusTypeChoice(models.TextChoices):
        inbound_scan = 'inbound-scan'
        scanned = 'scanned'
        transit = 'transit'
        in_transit = 'in-transit'
        delivery = 'delivery'

    tracking_number = models.CharField(max_length=20, db_index=True)
    carrier = models.CharField(max_length=20, choices=CarrierTypeChoice.choices, db_index=True)
    sender_address = models.CharField(max_length=200)
    receiver_address = models.CharField(max_length=200)
    receiver_city = models.CharField(max_length=45)
    receiver_country = models.CharField(max_length=45)
    receiver_zipcode = models.IntegerField()
    status = models.CharField(max_length=20, choices=StatusTypeChoice.choices, default=StatusTypeChoice.inbound_scan)
    weather = models.ForeignKey(Weather, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.tracking_number


class Articles(models.Model):
    SKU = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.SKU} "


class ShipmentArticle(models.Model):
    shipment = models.ForeignKey(Shipments, on_delete=models.CASCADE, null=False, related_name='quantity')
    article = models.ForeignKey(Articles, on_delete=models.PROTECT)
    quantity = models.IntegerField()
