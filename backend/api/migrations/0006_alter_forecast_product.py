# Generated by Django 4.2.5 on 2023-09-30 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_forecast_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forecast',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='api.product', verbose_name='Название продукта'),
            preserve_default=False,
        ),
    ]
