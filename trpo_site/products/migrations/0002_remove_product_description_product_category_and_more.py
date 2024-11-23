# Generated by Django 5.1.3 on 2024-11-23 17:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='Без категории', max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='incoming_date',
            field=models.DateField(default=datetime.datetime(2024, 11, 23, 20, 9, 15, 984551)),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
