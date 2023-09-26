from django_filters import rest_framework as filters

from .models import Stores


class ShopsFilter(filters.FilterSet):
    """Фильтр для магазинов."""
    class Meta:
        model = Stores
        fields = ['city', 'size', 'type_format', ]
