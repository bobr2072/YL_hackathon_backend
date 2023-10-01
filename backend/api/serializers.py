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
    units = serializers.IntegerField()
    date = serializers.DateField()

    class Meta:
        model = ProductPrediction
        fields = ['date', 'units']


class ProductSerialiazer(serializers.ModelSerializer):
    id = serializers.IntegerField(write_only=True)
    name = serializers.CharField()

    class Meta:
        model = Product
        fields = ('id', 'name')


class PredictionSerializer(serializers.ModelSerializer):
    product = ProductSerialiazer()
    predictions = ProductForPredictionSerializer()

    class Meta:
        model = Prediction
        fields = ['product', 'predictions']

    def to_internal_value(self, data):
        product_data = data.get('product')
        if isinstance(product_data, Product):
            data['product'] = product_data.pk
        obj = super(PredictionSerializer, self).to_internal_value(data)
        return obj


class ForecastPostSerializer(serializers.ModelSerializer):
    """Сериализатор записи прогноза."""
    store = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())
    predictions = PredictionSerializer()
    product = ProductSerialiazer()

    class Meta:
        model = Forecast
        fields = ['store', 'date', 'predictions', 'product']

    def create(self, validated_data):
        predictions_data = validated_data.pop('predictions')
        forecast = Forecast.objects.create(**validated_data)
        forecast.predictions.set(predictions_data)
        return forecast

# for prediction_data in predictions_data:
# prediction = Prediction(forecast=forecast)
# prediction_serializer = PredictionSerializer(prediction, data=prediction_data)
# if prediction_serializer.is_valid():
#  prediction_serializer.save()
# else:
# raise serializers.ValidationError(prediction_serializer.errors)
# return forecast


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
