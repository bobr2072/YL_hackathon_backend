from rest_framework import serializers

from api.models import (Categories, Forecast, Sales,
                        Stores, Profit, Prediction)


class ProfitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profit
        fields = ('date', 'type', 'units', 'units_promo', 'money', 'money_promo')


class SalesSerializer(serializers.ModelSerializer):
    """Сериализатор продаж."""
    store = serializers.CharField(source='store.name')
    saled_product = serializers.CharField(source='saled_product.name')
    profit = ProfitSerializer(many=True)

    class Meta:
        model = Sales
        fields = ('store', 'saled_product', 'profit')


class CategoriesSerializer(serializers.ModelSerializer):
    """Сериализатор категорий."""
    product = serializers.CharField(source='product.name')
    group = serializers.CharField(source='group.name')
    category = serializers.CharField(source='category.name')
    subcategory = serializers.CharField(source='subcategory.name')

    class Meta:
        model = Categories
        fields = ('product', 'group', 'category', 'subcategory', 'amount')


class PredictionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prediction
        fields = ('date', 'units')


class ForecastPostSerializer(serializers.ModelSerializer):
    store = serializers.CharField(source='store.name')
    prediction = PredictionSerializer(many=True)

    class Meta:
        model = Forecast
        fields = ('store', 'date', 'prediction')


class ForecastGetSerializer(serializers.ModelSerializer):
    store = serializers.CharField(source='store.name')
    product = serializers.CharField(source='product.name')
    prediction = PredictionSerializer(many=True)

    class Meta:
        model = Forecast
        fields = ('store', 'product', 'date', 'prediction')


class ShopsSerializer(serializers.ModelSerializer):
    """Сериализатор магазинов."""
    store_name = serializers.CharField(source='store_name.name')
    city = serializers.CharField(source='city.name')

    class Meta:
        model = Stores
        fields = ('store_name', 'city', 'division',
                  'type_format', 'loc', 'size',
                  'is_active')
