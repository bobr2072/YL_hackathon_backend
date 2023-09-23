from django.db import models


class Sales(models.Model):
    """Модель продаж."""
    st = models.IntegerField(
        unique=True,
        verbose_name='Захэшированное id магазина',
        db_index=True)
    pr_sku = models.IntegerField(
        unique=True,
        verbose_name='Захэшированное id товара',
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


class Categories(models.Model):
    """Модель категорий."""
    pass


class Shops(models.Model):
    """Модель магазинов."""
    pass


class Forecast(models.Model):
    """Модель предсказания."""
    pass
