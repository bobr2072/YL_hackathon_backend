# Generated by Django 4.2.5 on 2023-09-23 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st', models.IntegerField(db_index=True, unique=True, verbose_name='Захэшированное id магазина')),
                ('pr_sku', models.IntegerField(db_index=True, unique=True, verbose_name='Захэшированное id товара')),
                ('data', models.DateTimeField(verbose_name='Дата')),
                ('pr_sales_type', models.BooleanField(verbose_name='Флаг наличия промо')),
                ('pr_sales_in_units', models.IntegerField(verbose_name='Число проданных товаров без признака промо')),
                ('pr_promo_sales_in_units', models.IntegerField(verbose_name='Число проданных товаров с признаком промо')),
                ('pr_sales_in_rub', models.IntegerField(verbose_name='Продажи без признака промо в РУБ')),
                ('pr_promo_sales_in_rub', models.IntegerField(verbose_name='продажи с признаком промо в РУБ')),
            ],
        ),
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]