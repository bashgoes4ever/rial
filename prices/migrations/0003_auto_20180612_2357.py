# Generated by Django 2.0 on 2018-06-12 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0002_pricesfork_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricesfork',
            name='time',
            field=models.FloatField(default=0, verbose_name='Длительность ремонта на 1м2 (дней)'),
        ),
    ]