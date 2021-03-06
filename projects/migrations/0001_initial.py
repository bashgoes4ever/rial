# Generated by Django 2.0 on 2018-06-12 10:39

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default=None, null=True, upload_to='static/img/cases', verbose_name='Фото')),
                ('is_main', models.BooleanField(default=False, verbose_name='Главное фото')),
            ],
            options={
                'verbose_name': 'Фото проекта',
                'verbose_name_plural': 'Фото проектов',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Заголовок')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('time', models.IntegerField(default=0, verbose_name='Срок (дней)')),
                ('square', models.IntegerField(default=0, verbose_name='Площадь (м2)')),
                ('detail_page_content', tinymce.models.HTMLField(default=None, verbose_name='Контент детальной страницы')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Заголовок')),
                ('price', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Цена')),
                ('terms', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Сроки')),
                ('img', models.ImageField(blank=True, default=None, null=True, upload_to='static/img/block1', verbose_name='Фоновая картинка')),
                ('detail_page_content', tinymce.models.HTMLField(default=None, verbose_name='Контент детальной страницы')),
            ],
            options={
                'verbose_name': 'Тип помещения',
                'verbose_name_plural': 'Типы помещений',
            },
        ),
        migrations.AddField(
            model_name='projects',
            name='type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.ProjectType'),
        ),
        migrations.AddField(
            model_name='projectimages',
            name='project',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Projects'),
        ),
    ]
