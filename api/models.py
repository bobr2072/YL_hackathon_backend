from django.db import models


class Sales(models.Model):
    """Данные по продажам."""
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

# Я так понимаю, что тут должна быть не самая обычная модель, а иерархическая,
# как тут 2 ой пример
# https://qaa-engineer.ru/kak-ispolzovat-ierarhicheskuyu-peremennuyu-v-modeli-ml/)
