from django.db import models


class Stores(models.Model):
    """Модель магазинов."""

    store_name = models.CharField(
        max_length=32,
        verbose_name='Название магазина',
        primary_key=True
    )
    city = models.CharField(
        max_length=32,
        verbose_name='Город',
    )
    division = models.CharField(
        max_length=32,
        verbose_name='Подразделение',
    )
    type_format = models.PositiveIntegerField(
        verbose_name='Тип формата',
    )
    loc = models.PositiveIntegerField(
        verbose_name='Локация',
    )
    size = models.PositiveIntegerField(
        verbose_name='Размер',
    )
    is_active = models.BooleanField(
        verbose_name='Активен',
    )

    def __str__(self) -> str:
        return f'{self.store_name}'

    class Meta:
        unique_together = ('store_name', 'city')


class Profit(models.Model):
    """Модель выручки для продукта."""

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

    def __str__(self):
        return f'Продажи за {self.date}'


class Categories(models.Model):
    """Модель категорий."""

    product = models.CharField(
        max_length=32,
        verbose_name='Название товара'
    )
    store = models.ForeignKey(
        Stores,
        on_delete=models.DO_NOTHING,
        verbose_name='Магазин продаж',
    )
    group = models.CharField(
        max_length=32,
        verbose_name='Группа',
    )
    category = models.CharField(
        max_length=32,
        verbose_name='Категория',
    )
    subcategory = models.CharField(
        max_length=32,
        verbose_name='Подкатегория',
    )
    amount = models.PositiveIntegerField(
        verbose_name='Количество товара'
    )

    def __str__(self) -> str:
        return f'{self.product}'

    class Meta:
        unique_together = ('product', 'store')


class Sales(models.Model):
    """Модель продаж."""

    product_name = models.ForeignKey(
        Categories,
        on_delete=models.DO_NOTHING,
        verbose_name='Название товара'
    )
    store = models.ForeignKey(
        Stores,
        on_delete=models.DO_NOTHING,
        verbose_name='Магазин продаж',
    )
    profit = models.ManyToManyField(
        Profit,
        verbose_name='Информация о продажах товара'
    )

    def __str__(self) -> str:
        return f'{self.product_name}'


class Forecast(models.Model):
    """Модель прогноза для магазина и продукта."""

    store = models.ForeignKey(
        Stores,
        on_delete=models.DO_NOTHING,
        verbose_name='Прогноз для магазина'
    )
    product = models.ForeignKey(
        Categories,
        on_delete=models.DO_NOTHING,
        verbose_name='Название продукта'
    )
    forecast_date = models.DateField(
        verbose_name='Дата создания прогноза',
    )
    forecast = models.JSONField(default=dict)
