from rest_framework import serializers

from api.models import (Categories, Forecast, Prediction, Product,
                        ProductPrediction, Profit, Sales, Store, Stores)


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
        return ProductPrediction.objects.create(**validated_data)


class PredictionSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    prediction = ProductForPredictionSerializer()

    class Meta:
        model = Prediction
        fields = ['product', 'prediction']

    def create(self, validated_data):
        return Prediction.objects.create(**validated_data)


class ForecastPostSerializer(serializers.ModelSerializer):
    """Сериализатор записи прогноза."""
    store = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())
    predictions = PredictionSerializer()

    class Meta:
        model = Forecast
        fields = ['store', 'date', 'predictions']

    def add_product_predictions(self, date, units):
        ProductPrediction.objects.bulk_create(
            [ProductPrediction(
                date=date, units=units)
             ]
        )

    def add_prediction(self, product, model):
        model = self.add_product_predictions
        Prediction.objects.create(
            [Prediction(
                product=Product.objects.get(id=product['id']),
                model=model)
             ]
        )

    def create(self, data):
        predictions = data.pop('predictions')
        store = data.pop('store')
        product = data.pop('product')
        date = data.pop('date')
        forecast = Forecast.objects.create(store=store, product=product, date=date)
        forecast.predictions.set(predictions)
        self.add_prediction(product=product, model=predictions)
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
