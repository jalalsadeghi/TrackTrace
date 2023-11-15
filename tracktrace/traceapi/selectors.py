from django.db.models import QuerySet

from tracktrace.traceapi.models import Shipments
from tracktrace.traceapi.filters import TraceFilter


def get_traces(*, filters=None,) -> QuerySet[Shipments]:
    filters = filters or {}
    qs = Shipments.objects.filter()
    return TraceFilter(filters, qs).qs


def get_articles(shipment):
    articles = shipment.quantity.all().select_related('article')
    serialized_articles = []
    for article in articles:
        serialized_article = {
            'SKU': article.article.SKU,
            'name': article.article.name,
            'price': article.article.price,
            'quantity': article.quantity,
        }
        serialized_articles.append(serialized_article)
    return serialized_articles
