# Generated by Django 3.1.2 on 2020-10-16 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0004_auto_20201016_1750"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 10, 16, 17, 54, 8, 639198),
                editable=False,
            ),
        ),
    ]
