from rest_framework import viewsets

from api.models import Categories, Forecast, Sales, Stores
from api.serializers import (CategoriesSerializer, ForecastSerializer,
                             SalesSerializer, ShopsSerializer)


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer


class StoresViewSet(viewsets.ModelViewSet):
    queryset = Stores.objects.all()
    serializer_class = ShopsSerializer


class ForecastViewSet(viewsets.ModelViewSet):
    queryset = Forecast.objects.all()
    serializer_class = ForecastSerializer
