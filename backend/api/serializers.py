from rest_framework import serializers

from api.models import (Categories, Forecast, Profit, Sales, Stores)


class ProfitSerializer(serializers.ModelSerializer):
    type = serializers.IntegerField()

    class Meta:
        model = Profit
        fields = ['date', 'type', 'units',
                  'units_promo', 'money', 'money_promo']


class SalesSerializer(serializers.ModelSerializer):
    """Сериализатор продаж."""
    profit = ProfitSerializer(read_only=True, many=True)

    class Meta:
        model = Sales
        fields = ('store', 'product', 'profit')


class CategoriesSerializer(serializers.ModelSerializer):
    """Сериализатор категорий."""

    class Meta:
        model = Categories
        fields = ('product', 'group', 'category', 'subcategory', 'amount')


class StoresSerializer(serializers.ModelSerializer):
    """Сериализатор магазинов."""

    class Meta:
        model = Stores
        fields = ('store_name', 'city', 'division',
                  'type_format', 'loc', 'size',
                  'is_active')


class ForecastSerializer(serializers.ModelSerializer):
    """Сериализатор просмотра прогноза."""

    class Meta:
        model = Forecast
        fields = ['store', 'product', 'forecast_date', 'forecast']
