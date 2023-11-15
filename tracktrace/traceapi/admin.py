from django.contrib import admin
from tracktrace.traceapi.models import Shipments, Articles, ShipmentArticle


class ShipmentArticleInline(admin.TabularInline):
    model = ShipmentArticle
    extra = 1


@admin.register(Shipments)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['tracking_number', 'carrier']
    inlines = [ShipmentArticleInline]


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['SKU', 'name']
