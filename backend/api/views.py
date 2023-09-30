from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets

from api.models import Categories, Forecast, Sales, Stores
from api.serializers import (CategoriesSerializer, ForecastGetSerializer,
                             ForecastPostSerializer, SalesSerializer,
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
    filterset_fields = ['saled_product', 'store']


class StoresViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Stores.objects.all()
    serializer_class = ShopsSerializer


class ForecastViewSet(viewsets.ModelViewSet):
    queryset = Forecast.objects.all()

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return ForecastGetSerializer
        return ForecastPostSerializer

    def perform_create(self, serializer):
        serializer.save(product=self.request.POST.get('predictions.product'))
