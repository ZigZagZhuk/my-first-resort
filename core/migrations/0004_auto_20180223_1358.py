# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-23 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180223_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, default=None, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Название'),
        ),
    ]
