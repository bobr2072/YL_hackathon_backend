from django.db import models


class Category(models.Model):
    """Модель категории."""

    name = models.CharField(
        verbose_name='Название категории',
        max_length=32,
        unique=True,
        db_index=True,
    )


class Product(models.Model):
    """Модель товара."""

    name = models.CharField(
        verbose_name='Название товара',
        max_length=32,
        unique=True,
        db_index=True,
    )

    def __str__(self):
        return self.name


class Group(models.Model):
    """Модель группы."""

    name = models.CharField(
        verbose_name='Название группы',
        max_length=32,
        unique=True,
        db_index=True,
    )


class Subcategory(models.Model):
    """Модель подкатегории."""

    name = models.CharField(
        verbose_name='Название подкатегории',
        max_length=32,
        unique=True,
        db_index=True,
    )


class Store(models.Model):
    """Модель магазина."""

    name = models.CharField(
        verbose_name='Название магазина',
        max_length=32,
        unique=True,
        db_index=True
    )

    def __str__(self):
        return self.name


class City(models.Model):
    """Модель города."""

    name = models.CharField(
        verbose_name='Название города',
        max_length=32,
        unique=True,
        db_index=True,
    )


class Categories(models.Model):
    """Модель категорий."""

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Название товара',
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.DO_NOTHING,
        verbose_name='Группа',

    )
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        verbose_name='Категория',
    )
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.DO_NOTHING,
        verbose_name='Подкатегория',
    )
    amount = models.PositiveIntegerField(
        verbose_name='Количество товара'
    )


class Profit(models.Model):
    date = models.DateField(
        verbose_name='Дата продажи',
    )
    type = models.BooleanField(
        verbose_name='Промо или нет',
    )
    units = models.PositiveIntegerField(
        verbose_name='Число продаж без промо',
    )
    units_promo = models.PositiveIntegerField(
        verbose_name='Число продаж промо',
    )
    money = models.FloatField(
        verbose_name='Продажи без промо в РУБ',
    )
    money_promo = models.FloatField(
        verbose_name='Продажи промо в РУБ',
    )


class Sales(models.Model):
    """Модель продаж."""

    saled_product = models.ForeignKey(
        Product,
        on_delete=models.DO_NOTHING,
        verbose_name='Название товара',
    )
    store = models.ForeignKey(
        Store,
        on_delete=models.DO_NOTHING,
        verbose_name='Магазин продаж',
    )
    profit = models.ManyToManyField(
        Profit,
        verbose_name='Информация о продажах товара',
    )


class Stores(models.Model):
    """Модель магазинов."""

    store_name = models.ForeignKey(
        Store,
        on_delete=models.DO_NOTHING,
        verbose_name='Название магазина',
    )
    city = models.ForeignKey(
        City,
        on_delete=models.DO_NOTHING,
        verbose_name='Город',
    )
    division = models.CharField(
        max_length=32,
        verbose_name='Подразделение',
    )
    type_format = models.IntegerField(
        verbose_name='Тип формата',
    )
    loc = models.IntegerField(
        verbose_name='Локация',
    )
    size = models.IntegerField(
        verbose_name='Размер',
    )
    is_active = models.BooleanField(
        verbose_name='Активен',
    )

    class Meta:
        unique_together = ('store_name', 'city')


class ProductPrediction(models.Model):
    date = models.DateField(
        verbose_name='Дата продажи товара'
    )
    units = models.PositiveIntegerField(
        verbose_name='Ожидаемое кол-во продажи'
    )

    def __str__(self):
        return (f'{self.date}:{self.units}')


class Prediction(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.DO_NOTHING,
        verbose_name='Название продукта',
    )
    predictions = models.ForeignKey(
        ProductPrediction,
        on_delete=models.DO_NOTHING,
        verbose_name='Прогноз'
    )


class Forecast(models.Model):
    """Модель прогноза."""

    store = models.ForeignKey(
        Store,
        on_delete=models.DO_NOTHING,
        verbose_name='Прогноз для магазина'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.DO_NOTHING,
        verbose_name='Название продукта'
    )
    date = models.DateField(
        verbose_name='Дата прогноза',
    )
    product_prediction = models.ManyToManyField(
        ProductPrediction,
        verbose_name='Прогноз по продукту для магазина'
    )
    predictions = models.ManyToManyField(
        Prediction,
        verbose_name='Прогноз для продукта'
    )
