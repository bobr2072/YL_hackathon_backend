from rest_framework import serializers

from api.models import Categories, Forecast, Product, Profit, Sales, Stores


class ProfitSerializer(serializers.ModelSerializer):
    """Сериализатор выручки."""

    type = serializers.IntegerField()

    class Meta:
        model = Profit
        fields = ('date', 'type', 'units',
                  'units_promo', 'money', 'money_promo')


class SalesSerializer(serializers.ModelSerializer):
    """Сериализатор продаж товаров."""

    store = serializers.CharField(source='store.store_name')
    profit = ProfitSerializer(read_only=True, many=True)
    product = serializers.CharField(source='product.name')

    class Meta:
        model = Sales
        fields = ('store', 'product', 'profit')


class CategoriesSerializer(serializers.ModelSerializer):
    """Сериализатор категорий товаров."""

    store = serializers.PrimaryKeyRelatedField(queryset=Stores.objects.all())
    product = serializers.CharField(source='product.name')

    class Meta:
        model = Categories
        fields = ('store', 'product', 'group', 'category', 'subcategory', 'amount')


class StoresSerializer(serializers.ModelSerializer):
    """Сериализатор магазинов."""

    class Meta:
        model = Stores
        fields = ('store_name', 'city', 'division',
                  'type_format', 'loc', 'size',
                  'is_active')


class ForecastSerializer(serializers.ModelSerializer):
    """Сериализатор прогноза."""

    store = serializers.PrimaryKeyRelatedField(queryset=Stores.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Forecast
        fields = ('store', 'product', 'forecast_date', 'forecast')

    def create(self, validated_data):

        store_data = validated_data.pop('store')
        product_data = validated_data.pop('product')

        forecast = Forecast.objects.create(store=store_data, product=product_data, **validated_data)
        return forecast
