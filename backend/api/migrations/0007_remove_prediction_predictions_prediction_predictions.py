# Generated by Django 4.2.5 on 2023-09-30 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_forecast_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prediction',
            name='predictions',
        ),
        migrations.AddField(
            model_name='prediction',
            name='predictions',
            field=models.ManyToManyField(to='api.productprediction', verbose_name='Прогноз'),
        ),
    ]
