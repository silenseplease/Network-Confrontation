# Generated by Django 3.0.1 on 2020-03-15 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200315_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesession',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 15, 19, 32, 17, 708610)),
        ),
        migrations.AlterField(
            model_name='gamesession',
            name='date_started',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 15, 19, 32, 17, 708669)),
        ),
        migrations.AlterField(
            model_name='gamesession',
            name='date_stopped',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 15, 19, 32, 17, 708722)),
        ),
    ]
