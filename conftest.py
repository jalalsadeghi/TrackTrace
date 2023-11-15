import pytest
from tracktrace.tests.factories import (
    ShipmentsFactory,
    WeatherFactory,
    ArticlesFactory,
    ShipmentArticleFactory,
)


# تعریف متغییر برای یک سطر محوله
@pytest.fixture
def Shipment1():
    return ShipmentsFactory()


# تعریف متغییر برای یک سطر وضعیت هوای یک شهر
@pytest.fixture
def Weather1():
    return WeatherFactory()

#
# # تعریف متغییر برای یک سطر کالا
# @pytest.fixture
# def Articles1():
#     return ArticlesFactory()
#
#
# # تعریف متغییر برای یک سطر تعداد کالا درخواستی مشتری
# @pytest.fixture
# def ShipmentArticle1():
#     return ShipmentArticleFactory()


