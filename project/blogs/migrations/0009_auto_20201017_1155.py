# Generated by Django 3.1.2 on 2020-10-17 11:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_auto_20201017_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 17, 11, 55, 18, 296741), editable=False),
        ),
    ]