import requests
from datetime import timedelta
from django.utils import timezone

from tracktrace.weather.models import Weather
from tracktrace.traceapi.models import Shipments


def update_weather_data(receiver_city, receiver_country, receiver_zipcode):
    url = "https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}".format(
        city=receiver_city, country=receiver_country, api_key="1bb89c545856fe426c0b80071d7a2b9c"
    )
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        update, created = Weather.objects.update_or_create(
            city=receiver_city,
            country=receiver_country,
            zipcode=receiver_zipcode,
            defaults={
                "temperature": data["main"]["temp"],
                "wind_speed": data["wind"]["speed"],
            }
        )

        return timezone.now()


def shipment_weather_id(receiver_city, receiver_country, shipment_id):
    weather = Weather.objects.get(city=receiver_city, country=receiver_country)
    weather_id = weather.id
    Shipments.objects.filter(id=shipment_id).update(
        weather=weather_id
    )


def get_weather():
    for shipment in Shipments.objects.all():
        receiver_city = shipment.receiver_city
        receiver_country = shipment.receiver_country
        receiver_zipcode = shipment.receiver_zipcode
        shipment_id = shipment.id
        shipment_weather = shipment.weather_id

        update_city_if = True
        weather_if = Weather.objects.filter(city=receiver_city, country=receiver_country).exists()
        if weather_if:
            weather = Weather.objects.get(city=receiver_city, country=receiver_country)

            current_time = timezone.now()
            lastupdated = weather.updated_at
            timedifference = current_time - lastupdated

            update_city_if = timedifference > timedelta(minutes=1)

        if update_city_if:
            update_weather_data(receiver_city, receiver_country, receiver_zipcode)

        if shipment_weather is None:
            shipment_weather_id(receiver_city, receiver_country, shipment_id)
