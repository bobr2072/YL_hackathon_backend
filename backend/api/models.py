from django.db import models


class Categories(models.Model):
    """Модель категорий."""
    sku = models.TextField(
        'Артикул',
        unique=True)
    group = models.TextField(
        'Группа товаров',
        unique=True)
    category = models.TextField(
        'Категория товаров',
        unique=True)
    subcategory = models.TextField(
        'Подкатегория товаров',
        unique=True)
# Этот столбец(ИМХО) маркер, обозначающий продаётся товар на вес или в ШТ
# Мб здесь больше подходит тип Boolean?
    uom = models.IntegerField(
        'Единица измерения')


class SalesInStore(models.Model):
    """Связующая таблица для модели Sales."""
    date = models.DateField(
        'День продаж'
    )
    sales_units = models.IntegerField(
        'Число проданных товаров без признака промо')
    sales_units_promo = models.IntegerField(
        'Число проданных товаров c признаком промо')
    sales_rub = models.FloatField(
        'Продажи без признака промо в РУБ')
    subcatesales_run_promgory = models.FloatField(
        'Продажи с признаком промо в РУБ')


class Shops(models.Model):
    """Модель списка магазинов."""
    store = models.TextField(
        'Магаизн',
        unique=True)
    city = models.TextField(
        'Город')
    division = models.TextField(
        'Подразделение')
    type_format = models.IntegerField(
        'Формата магазина')
    loc = models.IntegerField(
        'Локация магазина')
    size = models.IntegerField(
        'Тип размера магазина')
    is_active = models.BooleanField(
        'Статус магазина(открыт/закрыт)')


class Sales(models.Model):
    """Модель продаж."""
    store = models.ForeignKey(
        'Магаизн',
        Shops,
        on_delete=models.CASCADE,
        db_index=True)
    sku = models.TextField(
        'Артикул',
        unique=True)
    fact = models.ForeignKey(
        'Продажи',
        SalesInStore,
        on_delete=models.CASCADE)


class SalesUnitsForForecast(models.Model):
    """Связующая таблица для модели ForecastInStore."""
    date = models.DateField(
        'Прогнозируемый день продаж'
    )
    quantity = models.IntegerField(
        'Прогнозируемое число продаж')


class ForecastInStore(models.Model):
    """Связующая таблица для модели Forecast."""
    sku = models.TextField(
        'Артикул',
        unique=True)
# Здесь должна быть связь с ещё одной таблицей?
    sales_units = models.ForeignKey(
        'Прогноз числа проданных товаров без признака промо',
        SalesUnitsForForecast,
        on_delete=models.CASCADE,
        db_index=True)


class Forecast(models.Model):
    """Модель прогнозов."""
    store = models.ForeignKey(
        'Магаизн',
        Shops,
        on_delete=models.CASCADE,
        db_index=True)
    forecast_date = models.DateField(
        'Дата прогноза'
    )
    forecast = models.ForeignKey(
        'Прогноз',
        ForecastInStore,
        on_delete=models.CASCADE)
