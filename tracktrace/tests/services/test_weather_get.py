import pytest

from datetime import timedelta
from django.utils import timezone

from tracktrace.weather.services import get_weather, update_weather_data


@pytest.mark.django_db
def test_get_weather():
    a = get_weather()


@pytest.mark.django_db
def test_update_weather_data():
    a = update_weather_data("Paris", "France", 75001)

    current_time = timezone.now()
    last_updated = a
    time_difference = current_time - last_updated

    assert time_difference < timedelta(minutes=1)
