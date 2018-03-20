# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-23 12:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180223_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, default=None, verbose_name='Номер')),
                ('number_of_bed', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=None, verbose_name='Количество мест')),
                ('shower', models.CharField(blank=True, choices=[('Yes', 'Да'), ('No', 'Нет')], default=None, max_length=3, verbose_name='Душ')),
                ('category', models.CharField(blank=True, choices=[('Lux', 'Люкс'), ('Half_Lux', 'Полулюкс'), ('Standart', 'Стандарт'), ('Econom', 'Эконом')], default=None, max_length=10, verbose_name='Тип номера')),
            ],
            options={
                'verbose_name': 'Стол',
                'verbose_name_plural': 'Столы',
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, default=None, verbose_name='Номер')),
                ('number_of_guests', models.IntegerField(default=None, verbose_name='Количество персон')),
            ],
            options={
                'verbose_name': 'Стол',
                'verbose_name_plural': 'Столы',
            },
        ),
        migrations.AddField(
            model_name='guest',
            name='data_arrival',
            field=models.DateTimeField(default=None, null=True, verbose_name='Дата приезда'),
        ),
        migrations.AddField(
            model_name='guest',
            name='data_departure',
            field=models.DateTimeField(default=None, null=True, verbose_name='Дата отъезда'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='age',
            field=models.IntegerField(default=0, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='name',
            field=models.CharField(blank=True, max_length=64, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='patronomic',
            field=models.CharField(max_length=64, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='sex',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default=None, max_length=6, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='surname',
            field=models.CharField(blank=True, max_length=64, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='guest',
            name='room',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Room', verbose_name='Комната'),
        ),
        migrations.AddField(
            model_name='guest',
            name='table',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Table', verbose_name='Стол'),
        ),
    ]
