from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from tracktrace.api.pagination import LimitOffsetPagination, get_paginated_response_context

from drf_spectacular.utils import extend_schema

from tracktrace.traceapi.models import Shipments
from tracktrace.traceapi.selectors import get_traces, get_articles


class TraceApi(APIView):
    class Pagination(LimitOffsetPagination):
        default_limit = 10

    class FilterTraceSerializer(serializers.Serializer):

        search = serializers.CharField(required=False, max_length=100)
        tracking_number = serializers.CharField(required=False, max_length=20)
        carrier = serializers.CharField(required=False, max_length=20)

    class OutputTraceSerializer(serializers.ModelSerializer):

        class Meta:
            model = Shipments
            fields = ("tracking_number", "carrier", "status", "sender_address", "receiver_address", "articles", "weather")

        articles = serializers.SerializerMethodField('get_articles')
        weather = serializers.SerializerMethodField('get_weather')

        def get_articles(self, shipment):
            return get_articles(shipment)

        def get_weather(self, shipment):
            weather = shipment.weather
            if weather is not None:
                serialized_weather = {
                    'temperature': weather.temperature,
                    'wind_speed': weather.wind_speed,
                }
                return serialized_weather

    @extend_schema(
        parameters=[FilterTraceSerializer],
        responses=OutputTraceSerializer
    )
    def get(self, request):
        filters_serializer = self.FilterTraceSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        try:
            query = get_traces(filters=filters_serializer.validated_data).select_related('weather')
        except Exception as ex:
            return Response(
                {"detail": "Filter Error - " + str(ex)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        data = get_paginated_response_context(
            pagination_class=self.Pagination,
            serializer_class=self.OutputTraceSerializer,
            queryset=query,
            request=request,
            view=self,
        )
        return data

