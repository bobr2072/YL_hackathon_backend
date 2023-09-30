from django.contrib import admin

from api.models import (Categories, Category, City, Forecast, Group,
                        Prediction, Product, ProductPrediction, Profit, Sales,
                        Store, Stores, Subcategory)


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('saled_product', 'store', 'profit_list')
    filter_horizontal = ('profit',)

    def profit_list(self, obj):
        return ", ".join([str(profit.date) for profit in obj.profit.all()])
    profit_list.short_description = 'Даты продаж'


@admin.register(Stores)
class StoresAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('store_name', 'city', 'division', 'type_format', 'loc', 'size', 'is_active')


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('product', 'group', 'category', 'subcategory', 'amount')


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('store', 'product', 'date')
    filter_horizontal = ('product_prediction', 'predictions')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('name', )


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('name', )


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('name', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('name', )


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('name', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('name', )


@admin.register(Profit)
class ProfitAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('date', 'type', 'units', 'units_promo', 'money', 'money_promo')


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('product', 'predictions_list')
    filter_horizontal = ('predictions',)

    def predictions_list(self, obj):
        return ", ".join([str(prediction.date) for prediction in obj.predictions.all()])
    predictions_list.short_description = 'Прогноз'


@admin.register(ProductPrediction)
class ProductPredictionAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('date', 'units')
