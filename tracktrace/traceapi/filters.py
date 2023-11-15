from django_filters import (
    CharFilter,
    FilterSet,
)
from django.contrib.postgres.search import SearchVector
from tracktrace.traceapi.models import Shipments


class TraceFilter(FilterSet):

    tracking_number = CharFilter(method="filter_tracking_number")
    carrier = CharFilter(method="filter_carrier")
    search = CharFilter(method="filter_search")

    def filter_tracking_number(self, queryset, name, value):
        return queryset.annotate(search=SearchVector("tracking_number")).filter(tracking_number=value)

    def filter_carrier(self, queryset, name, value):
        return queryset.annotate(search=SearchVector("carrier")).filter(carrier=value)

    def filter_search(self, queryset, name, value):
        return queryset.annotate(search=SearchVector("tracking_number", "carrier", "receiver_city")).filter(search=value)

    class Meta:
        model = Shipments
        fields = (
            "tracking_number",
            "carrier",
        )