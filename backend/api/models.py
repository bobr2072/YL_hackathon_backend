from django.db import models


class Categories(models.Model):
    """Модель категорий."""
    sku = models.TextField(
        unique=True,
        verbose_name='Артикул',
        db_index=True)
    group = models.TextField(
        unique=True,
        verbose_name='Группа товаров',
        db_index=True)
    category = models.TextField(
        unique=True,
        verbose_name='Категория товаров',
        db_index=True)
    subcategory = models.TextField(
        unique=True,
        verbose_name='Подкатегория товаров',
        db_index=True)
# Этот столбец(ИМХО) маркер, обозначающий продаётся товар на вес или в ШТ
# Мб здесь больше подходит тип Boolean?
    uom = models.IntegerField(
        verbose_name='Единица измерения')


class SalesInStore(models.Model):
    """Связующая таблица для модели Sales."""
    date = models.DateField(
        verbose_name='День продаж'
    )
    sales_units = models.IntegerField(
        verbose_name='Число проданных товаров без признака промо',
        db_index=True)
    sales_units_promo = models.IntegerField(
        verbose_name='Число проданных товаров c признаком промо',
        db_index=True)
    sales_rub = models.FloatField(
        verbose_name='Продажи без признака промо в РУБ',
        db_index=True)
    subcatesales_run_promgory = models.FloatField(
        verbose_name='Продажи с признаком промо в РУБ',
        db_index=True)


class Shops(models.Model):
    """Модель списка магазинов."""
    store = models.TextField(
        unique=True,
        verbose_name='Магаизн',
        db_index=True)
    city = models.TextField(
        verbose_name='Город',
        db_index=True)
    division = models.TextField(
        verbose_name='Подразделение',
        db_index=True)
    type_format = models.IntegerField(
        verbose_name='Формата магазина',
        db_index=True)
    loc = models.IntegerField(
        verbose_name='Локация магазина',
        db_index=True)
    size = models.IntegerField(
        verbose_name='Тип размера магазина',
        db_index=True)
    is_active = models.BooleanField(
        verbose_name='Статус магазина(открыт/закрыт)',
        db_index=True)


class Sales(models.Model):
    """Данные по продажам."""
    st = models.IntegerField(
        unique=True,
        verbose_name='Артикул',
        db_index=True)
    fact = models.ForeignKey(
        SalesInStore,
        on_delete=models.CASCADE,
        verbose_name='Продажи')


class SalesUnitsForForecast(models.Model):
    """Связующая таблица для модели ForecastInStore."""
    date = models.DateField(
        verbose_name='Прогнозируемый день продаж'
    )
    quantity = models.IntegerField(
        verbose_name='Прогнозируемое число продаж',
        db_index=True)


class ForecastInStore(models.Model):
    """Связующая таблица для модели Forecast."""
    sku = models.TextField(
        unique=True,
        verbose_name='Артикул',
        db_index=True)
# Здесь должна быть связь с ещё одной таблицей?
    sales_units = models.ForeignKey(
        SalesUnitsForForecast,
        on_delete=models.CASCADE,
        verbose_name='Прогноз числа проданных товаров без признака промо',
        db_index=True)
    data = models.DateTimeField(
        verbose_name='Дата')
    pr_sales_type = models.BooleanField(
        verbose_name='Флаг наличия промо')
    pr_sales_in_units = models.IntegerField(
        verbose_name='Число проданных товаров без признака промо')
    pr_promo_sales_in_units = models.IntegerField(
        verbose_name='Число проданных товаров с признаком промо')
    pr_sales_in_rub = models.IntegerField(
        verbose_name='Продажи без признака промо в РУБ')
    pr_promo_sales_in_rub = models.IntegerField(
        verbose_name='продажи с признаком промо в РУБ')

# Я так понимаю, что тут должна быть не самая обычная модель, а иерархическая,
# как тут 2 ой пример
# https://qaa-engineer.ru/kak-ispolzovat-ierarhicheskuyu-peremennuyu-v-modeli-ml/)
