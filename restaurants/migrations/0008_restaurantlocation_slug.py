# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('restaurants', '0007_auto_20170624_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
