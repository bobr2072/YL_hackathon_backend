# Generated by Django 4.2.5 on 2023-09-27 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=32, unique=True, verbose_name='Название категории')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=32, unique=True, verbose_name='Название города')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=32, unique=True, verbose_name='Название группы')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=32, unique=True, verbose_name='Название товара')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата продажи товара')),
                ('units', models.PositiveIntegerField(verbose_name='Ожидаемое кол-во продажи')),
            ],
        ),
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
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=32, unique=True, verbose_name='Название магазина')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=32, unique=True, verbose_name='Название подкатегории')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profit', models.ManyToManyField(to='api.profit', verbose_name='Информация о продажах товара')),
                ('saled_product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.product', verbose_name='Название товара')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.store', verbose_name='Магазин продаж')),
            ],
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prediction', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.productprediction', verbose_name='Прогноз')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.product', verbose_name='Название продукта')),
            ],
        ),
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата прогноза')),
                ('prediction', models.ManyToManyField(to='api.prediction', verbose_name='Прогноз для продукта')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.store', verbose_name='Прогноз для магазина')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Количество товара')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.category', verbose_name='Категория')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.group', verbose_name='Группа')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product', verbose_name='Название товара')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.subcategory', verbose_name='Подкатегория')),
            ],
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(max_length=32, verbose_name='Подразделение')),
                ('type_format', models.IntegerField(verbose_name='Тип формата')),
                ('loc', models.IntegerField(verbose_name='Локация')),
                ('size', models.IntegerField(verbose_name='Размер')),
                ('is_active', models.BooleanField(verbose_name='Активен')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.city', verbose_name='Город')),
                ('store_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.store', verbose_name='Название магазина')),
            ],
            options={
                'unique_together': {('store_name', 'city')},
            },
        ),
    ]
