from rest_framework import serializers

from api.models import Categories, Forecast, Profit, Sales, Stores


class ProfitSerializer(serializers.ModelSerializer):
    type = serializers.IntegerField()

    class Meta:
        model = Profit
        fields = ('date', 'type', 'units',
                  'units_promo', 'money', 'money_promo')


class SalesSerializer(serializers.ModelSerializer):
    """Сериализатор продаж."""
    store = serializers.CharField(source='store.store_name')
    profit = ProfitSerializer(read_only=True, many=True)

    class Meta:
        model = Sales
        fields = ('store', 'product_name', 'profit')


class CategoriesSerializer(serializers.ModelSerializer):
    """Сериализатор категорий."""
    product = serializers.CharField(source='product.product_name')

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
    store = serializers.PrimaryKeyRelatedField(queryset=Stores.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Sales.objects.all())

    class Meta:
        model = Forecast
        fields = ('store', 'product', 'forecast_date', 'forecast')

    def create(self, validated_data):

        store_data = validated_data.pop('store')
        product_data = validated_data.pop('product')

        forecast = Forecast.objects.create(store=store_data, product=product_data, **validated_data)
        return forecast
