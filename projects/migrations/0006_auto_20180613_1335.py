# Generated by Django 2.0 on 2018-06-13 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20180612_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='slug',
            field=models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='URL страницы'),
        ),
        migrations.AddField(
            model_name='projecttype',
            name='slug',
            field=models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='URL страницы'),
        ),
    ]
