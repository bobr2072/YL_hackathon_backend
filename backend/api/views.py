from rest_framework import viewsets

from api.filters import ShopsFilter
from api.models import Categories, Forecast, Sales, Shops
from api.serializers import (CategoriesSerializer, ForecastSerializer,
                             SalesSerializer, ShopsSerializer)


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories
    serializer_class = CategoriesSerializer


class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales
    serializer_class = SalesSerializer


class ShopsViewSet(viewsets.ModelViewSet):
    queryset = Shops
    serializer_class = ShopsSerializer
    filterset_class = ShopsFilter


class ForecastViewSet(viewsets.ModelViewSet):
    queryset = Forecast
    serializer_class = ForecastSerializer
