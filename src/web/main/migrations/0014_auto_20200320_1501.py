# Generated by Django 3.0.1 on 2020-03-20 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20200318_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesession',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 20, 15, 1, 47, 922680)),
        ),
        migrations.AlterField(
            model_name='gamesession',
            name='date_started',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 20, 15, 1, 47, 922718)),
        ),
        migrations.AlterField(
            model_name='gamesession',
            name='date_stopped',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 20, 15, 1, 47, 922752)),
        ),
    ]
