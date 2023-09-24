from django_filters import rest_framework as filters

from .models import Shops


class ShopsFilter(filters.FilterSet):
    """Фильтр для магазинов."""
    class Meta:
        model = Shops
        fields = ['city', 'size', 'type_format', ]
