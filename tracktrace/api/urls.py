from django.urls import path, include

urlpatterns = [
    path('traceapi/', include(('tracktrace.traceapi.urls', 'traceapi')))
]
