# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-23 10:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180223_1347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорию', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='guest',
            options={'verbose_name': 'Постоялеца', 'verbose_name_plural': 'Постояльцы'},
        ),
    ]
