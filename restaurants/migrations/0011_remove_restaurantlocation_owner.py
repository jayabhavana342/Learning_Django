# Generated by Django 2.0.1 on 2018-01-13 19:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('restaurants', '0010_restaurantlocation_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantlocation',
            name='owner',
        ),
    ]