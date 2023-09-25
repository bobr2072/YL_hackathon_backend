from django.contrib import admin

from api.models import (Categories, Category, City, Forecast, Group,
                        Prediction, Product, Profit, Sales, Store, Stores,
                        Subcategory)


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    ordering = ('id',)


@admin.register(Categories)
class TagAdmin(admin.ModelAdmin):
    ordering = ('id',)


@admin.register(Group)
class IngredientAdmin(admin.ModelAdmin):
    ordering = ('id',)


@admin.register(Store)
class CartAdmin(admin.ModelAdmin):
    ordering = ('id',)


@admin.register(Stores)
class FavoriteAdmin(admin.ModelAdmin):
    ordering = ('id',)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    ordering = ('id',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ('id',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    ordering = ('id',)


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    ordering = ('id',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ('id',)


@admin.register(Profit)
class ProfitAdmin(admin.ModelAdmin):
    ordering = ('id',)


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    ordering = ('id',)
