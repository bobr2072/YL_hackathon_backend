# Generated by Django 4.2.5 on 2023-10-08 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sales',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='categories',
            unique_together={('product', 'store')},
        ),
    ]
