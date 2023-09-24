from rest_framework import serializers

from api.models import Categories, Forecast, Sales, Shops


class SalesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sales
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'


class ForecastSerializer(serializers.ModelSerializer):

    class Meta:
        model = Forecast
        fields = '__all__'


class ShopsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shops
        fields = '__all__'
