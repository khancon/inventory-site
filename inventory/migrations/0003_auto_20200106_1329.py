# Generated by Django 2.1.7 on 2020-01-06 18:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20200106_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(default=None, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='zip_code',
            field=models.IntegerField(default=None, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(0)]),
        ),
    ]