from rest_framework import serializers

from api.models import (Categories, Forecast, Prediction, ProductPrediction,
                        Profit, Sales, Stores, Store, Product)


class ProfitSerializer(serializers.ModelSerializer):
    type = serializers.IntegerField()

    class Meta:
        model = Profit
        fields = ['date', 'type', 'units',
                  'units_promo', 'money', 'money_promo']


class SalesSerializer(serializers.ModelSerializer):
    """Сериализатор продаж."""
    store = serializers.CharField(source='store.name')
    saled_product = serializers.CharField(source='saled_product.name')
    profit = ProfitSerializer(read_only=True, many=True)

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


class ProductForPredictionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductPrediction
        fields = ['date', 'units']

    def create(self, validated_data):
        return ProductPrediction(**validated_data)


class PredictionSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    prediction = ProductForPredictionSerializer()

    class Meta:
        model = Prediction
        fields = ['product', 'prediction']

    def create(self, validated_data):
        return Prediction(**validated_data)


class ForecastPostSerializer(serializers.ModelSerializer):
    """Сериализатор записи прогноза."""
    store = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())
    predictions = PredictionSerializer()

    class Meta:
        model = Forecast
        fields = ['store', 'date', 'predictions']

    def create(self, validated_data):
        predictions = validated_data.pop('predictions')
        store = validated_data.pop('store')
        product = validated_data.pop('product')
        date = validated_data.pop('date')
        forecast = Forecast.objects.create(product=product, date=date, store=store)
        forecast.predictions.set(predictions)
        return forecast


class ForecastGetSerializer(serializers.ModelSerializer):
    """Сериализатор просмотра прогноза."""
    store = serializers.CharField(source='store.name')
    product = serializers.CharField(source='product.name')
    product_prediction = serializers.StringRelatedField(many=True)

    class Meta:
        model = Forecast
        fields = ['store', 'product', 'date', 'product_prediction']


class ShopsSerializer(serializers.ModelSerializer):
    """Сериализатор магазинов."""
    store_name = serializers.CharField(source='store_name.name')
    city = serializers.CharField(source='city.name')
    is_active = serializers.IntegerField()

    class Meta:
        model = Stores
        fields = ('store_name', 'city', 'division',
                  'type_format', 'loc', 'size',
                  'is_active')
