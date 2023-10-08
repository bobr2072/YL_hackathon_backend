# Generated by Django 4.2.5 on 2023-10-08 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата продажи')),
                ('type', models.BooleanField(verbose_name='Промо или нет')),
                ('units', models.PositiveIntegerField(verbose_name='Число продаж без промо')),
                ('units_promo', models.PositiveIntegerField(verbose_name='Число продаж промо')),
                ('money', models.FloatField(verbose_name='Продажи без промо в РУБ')),
                ('money_promo', models.FloatField(verbose_name='Продажи промо в РУБ')),
            ],
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('store_name', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='Название магазина')),
                ('city', models.CharField(max_length=32, verbose_name='Город')),
                ('division', models.CharField(max_length=32, verbose_name='Подразделение')),
                ('type_format', models.PositiveIntegerField(verbose_name='Тип формата')),
                ('loc', models.PositiveIntegerField(verbose_name='Локация')),
                ('size', models.PositiveIntegerField(verbose_name='Размер')),
                ('is_active', models.BooleanField(verbose_name='Активен')),
            ],
            options={
                'unique_together': {('store_name', 'city')},
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=32, verbose_name='Название товара')),
                ('profit', models.ManyToManyField(to='api.profit', verbose_name='Информация о продажах товара')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.stores', verbose_name='Магазин продаж')),
            ],
        ),
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forecast_date', models.DateField(verbose_name='Дата создания прогноза')),
                ('forecast', models.JSONField(default=dict)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.sales', verbose_name='Название продукта')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.stores', verbose_name='Прогноз для магазина')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=32, verbose_name='Группа')),
                ('category', models.CharField(max_length=32, verbose_name='Категория')),
                ('subcategory', models.CharField(max_length=32, verbose_name='Подкатегория')),
                ('amount', models.PositiveIntegerField(verbose_name='Количество товара')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.sales', verbose_name='Название товара')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.stores', verbose_name='Магазин продаж')),
            ],
        ),
    ]
