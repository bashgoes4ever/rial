# Generated by Django 2.0 on 2018-06-12 13:38

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Тип помещения')),
            ],
            options={
                'verbose_name': 'Тип помещения',
                'verbose_name_plural': 'Типы помещений в калькуляторе',
            },
        ),
        migrations.CreateModel(
            name='PricesFork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Название')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('img', models.ImageField(blank=True, default=None, null=True, upload_to='static/img/block6', verbose_name='Фоновая картинка')),
                ('content', tinymce.models.HTMLField(default=None, verbose_name='Контент на детальной странице')),
            ],
            options={
                'verbose_name': 'Тип ремонта',
                'verbose_name_plural': 'Типы ремонтов',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Название')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('content', tinymce.models.HTMLField(default=None, verbose_name='Контент на детальной странице')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='ServicesCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Название')),
                ('content', tinymce.models.HTMLField(default=None, verbose_name='Контент на детальной странице')),
            ],
            options={
                'verbose_name': 'Вид работ',
                'verbose_name_plural': 'Виды работ',
            },
        ),
        migrations.AddField(
            model_name='services',
            name='categorie',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='prices.ServicesCategories'),
        ),
    ]