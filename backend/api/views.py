from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from api.models import Categories, Forecast, Sales, Stores
from api.serializers import (CategoriesSerializer, ForecastSerializer,
                             SalesSerializer, StoresSerializer)


class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    """Вььюсет категорий товаров."""

    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['product__name', 'group', 'category', 'subcategory']


class SalesViewSet(viewsets.ReadOnlyModelViewSet):
    """Вььюсет продаж товаров."""

    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product', 'store']


class StoresViewSet(viewsets.ReadOnlyModelViewSet):
    """Вььюсет магазинов."""

    queryset = Stores.objects.all()
    serializer_class = StoresSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['store_name', 'city', 'division']


class ForecastViewSet(viewsets.ModelViewSet):
    """Вььюсет прогноза."""

    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['product']
