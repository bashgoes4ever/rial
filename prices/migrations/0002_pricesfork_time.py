# Generated by Django 2.0 on 2018-06-12 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricesfork',
            name='time',
            field=models.IntegerField(default=0, verbose_name='Длительность ремонта на 1м2'),
        ),
    ]
