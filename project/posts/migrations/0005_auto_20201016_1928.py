# Generated by Django 3.1.2 on 2020-10-16 19:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_auto_20201016_1847"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 10, 16, 19, 28, 0, 429388),
                editable=False,
            ),
        ),
    ]
