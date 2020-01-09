# Generated by Django 2.1.7 on 2020-01-06 18:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default=None, max_length=250)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('stock_quantity', models.IntegerField(default=None, max_length=10)),
                ('description', models.CharField(default=None, max_length=1000)),
                ('photo', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(default=None, max_length=10, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999999)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='zip_code',
            field=models.CharField(default=None, max_length=5, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(0)]),
        ),
    ]