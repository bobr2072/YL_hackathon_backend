from django.contrib import admin

from api.models import Categories, Forecast, Product, Profit, Sales, Stores


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ('name',)


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    ordering = ('product',)
    list_display = ('product', 'store', 'profit_list')
    filter_horizontal = ('profit',)

    def profit_list(self, obj):
        return ", ".join([str(profit.date) for profit in obj.profit.all()])
    profit_list.short_description = 'Даты продаж'


@admin.register(Stores)
class StoresAdmin(admin.ModelAdmin):
    ordering = ('store_name',)
    list_display = ('store_name', 'city', 'division', 'type_format', 'loc', 'size', 'is_active')


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    ordering = ('product',)
    list_display = ('product', 'group', 'category', 'subcategory', 'amount')


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('store', 'product', 'forecast_date', 'forecast')


@admin.register(Profit)
class ProfitAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('date', 'type', 'units', 'units_promo', 'money', 'money_promo')
