from rest_framework import viewsets

from api.models import Categories, Forecast, Sales, Shops
from api.serializers import (CategoriesSerializer, ForecastSerializer,
                             SalesSerializer, ShopsSerializer)


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer


class ShopsViewSet(viewsets.ModelViewSet):
    queryset = Shops.objects.all()
    serializer_class = ShopsSerializer


class ForecastViewSet(viewsets.ModelViewSet):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer
