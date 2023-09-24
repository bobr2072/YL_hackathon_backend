from rest_framework import serializers

from api.models import Categories, Forecast, Sales, Shops


class SalesSerializer(serializers.ModelSerializer):
    # fact = FactInStoreSerializer(many=True) - как пример

    class Meta:
        model = Sales
        fields = ('store', 'sku', 'fact')


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        # Может, сюда лучше указать read_only_fields ?
        fields = ('sku', 'group', 'category', 'subcategory', 'uom')


class ForecastSerializer(serializers.ModelSerializer):
    store = serializers.ReadOnlyField(sourse='shops.store')
    # forecast = ForecastForSalesSerializer(many=True) - как пример

    class Meta:
        model = Forecast
        fields = ('store', 'forecast_date', 'forecast')


class ShopsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shops
        fields = ('store', 'city', 'division',
                  'type_format', 'loc', 'size',
                  'is_active')
