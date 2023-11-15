import factory

from tracktrace.traceapi.models import Shipments, Articles, ShipmentArticle
from tracktrace.weather.models import Weather
from django.utils import timezone


class WeatherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Weather

    city = factory.LazyAttribute(lambda _: f'{"Paris"}')
    country = factory.LazyAttribute(lambda _: f'{"France"}')
    temperature = factory.LazyAttribute(lambda _: f'{20}')
    wind_speed = factory.LazyAttribute(lambda _: f'{5}')
    zipcode = factory.LazyAttribute(lambda _: f'{75001}')
    created_at = factory.LazyAttribute(lambda _: f'{timezone.now()}')
    updated_at = factory.LazyAttribute(lambda _: f'{timezone.now()}')


class ShipmentsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Shipments

    tracking_number = factory.LazyAttribute(lambda _: f'{"TN12345678"}')
    carrier = factory.LazyAttribute(lambda _: f'{"DHL"}')
    sender_address = factory.LazyAttribute(lambda _: f'{"Street 1, 10115 Berlin, Germany"}')
    receiver_address = factory.LazyAttribute(lambda _: f'{"Street 10, 75001 Paris,France"}')
    receiver_city = factory.LazyAttribute(lambda _: f'{"Paris"}')
    receiver_country = factory.LazyAttribute(lambda _: f'{"France"}')
    receiver_zipcode = factory.LazyAttribute(lambda _: f'{"75001"}')
    status = factory.LazyAttribute(lambda _: f'{"in-transit"}')
    weather = factory.SubFactory(WeatherFactory)
    created_at = factory.LazyAttribute(lambda _: f'{timezone.now()}')
    updated_at = factory.LazyAttribute(lambda _: f'{timezone.now()}')


class ArticlesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Articles

    SKU = factory.LazyAttribute(lambda _: f'{"LP123"}')
    name = factory.LazyAttribute(lambda _: f'{"Laptop"}')
    price = factory.LazyAttribute(lambda _: f'{800}')


class ShipmentArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ShipmentArticle

    shipment = factory.SubFactory(ShipmentsFactory)
    article = factory.SubFactory(ArticlesFactory)
    quantity = factory.LazyAttribute(lambda _: f'{1}')



