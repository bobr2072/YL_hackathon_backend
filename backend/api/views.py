from rest_framework import permissions, viewsets

from api.filters import SalesFilter, ShopsFilter
from api.models import Categories, Forecast, Sales, Stores
from api.serializers import (CategoriesSerializer, ForecastGetSerializer,
                             ForecastPostSerializer, SalesSerializer,
                             ShopsSerializer)


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    filterset_class = SalesFilter


class StoresViewSet(viewsets.ModelViewSet):
    queryset = Stores.objects.all()
    serializer_class = ShopsSerializer
    filterset_class = ShopsFilter


class ForecastViewSet(viewsets.ModelViewSet):
    queryset = Forecast.objects.all()

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return ForecastGetSerializer
        return ForecastPostSerializer
