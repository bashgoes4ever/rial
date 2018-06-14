# Generated by Django 2.0 on 2018-06-13 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_delete_block1main'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Адрес')),
                ('time', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Время работы')),
                ('email', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='E-mail')),
                ('map', models.TextField(blank=True, default=None, null=True, verbose_name='Код карты (ширину и высоту на 100%)')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='ContactsBusiness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Реквизиты (инн, кпп и т.д.)')),
                ('contact', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Contacts')),
            ],
            options={
                'verbose_name': 'Реквизиты',
                'verbose_name_plural': 'Реквизиты',
            },
        ),
        migrations.CreateModel(
            name='ContactsPhones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Телефон')),
                ('contact', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Contacts')),
            ],
            options={
                'verbose_name': 'Телефоны',
                'verbose_name_plural': 'Номера телефонов',
            },
        ),
        migrations.CreateModel(
            name='Socials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('href', models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Ссылка')),
                ('img', models.ImageField(blank=True, default=None, null=True, upload_to='static/img/', verbose_name='Иконка')),
                ('contact', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Contacts')),
            ],
            options={
                'verbose_name': 'Соц сеть',
                'verbose_name_plural': 'Соц сети',
            },
        ),
    ]
