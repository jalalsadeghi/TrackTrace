from celery import shared_task
from tracktrace.weather.services import get_weather


@shared_task
def weather_update():
    get_weather()
