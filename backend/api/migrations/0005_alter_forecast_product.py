# Generated by Django 4.2.5 on 2023-09-30 12:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_prediction_prediction_predictions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forecast',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.product', verbose_name='Название продукта'),
        ),
    ]
