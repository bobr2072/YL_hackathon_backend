from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from api.models import Categories, Forecast, Sales, Stores
from api.serializers import (CategoriesSerializer,
                             ForecastSerializer, SalesSerializer,
                             ShopsSerializer)


class CategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['product__name']


class SalesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product', 'store']


class StoresViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stores.objects.all()
    serializer_class = ShopsSerializer


class ForecastViewSet(viewsets.ModelViewSet):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer
