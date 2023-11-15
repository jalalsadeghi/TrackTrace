from django.urls import path
from tracktrace.traceapi.apis import TraceApi


app_name = "traceapi"
urlpatterns = [
        path("trace/", TraceApi.as_view(), name="trace"),
]