# Generated by Django 2.0 on 2018-06-13 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0003_auto_20180612_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='img',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='static/img/block6', verbose_name='Фоновая картинка'),
        ),
    ]
