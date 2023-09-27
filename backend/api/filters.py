from django_filters import rest_framework as filters

from .models import Stores, Sales


class ShopsFilter(filters.FilterSet):
    """Фильтр для магазинов."""
    class Meta:
        model = Stores
        fields = ['city', 'size', 'type_format', ]


class SalesFilter(filters.FilterSet):
    """Фильтр для продаж."""
    class Meta:
        model = Sales
        fields = ['saled_product', 'store']
