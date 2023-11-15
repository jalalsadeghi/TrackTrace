import pytest

from tracktrace.traceapi.selectors import get_traces


@pytest.mark.django_db
def test_shipment_search_True(Shipment1):
    a = get_traces()
    assert a.first() == Shipment1
