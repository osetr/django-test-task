# Generated by Django 3.1.2 on 2020-10-16 18:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blogs", "0005_auto_20201016_1754"),
    ]

    operations = [
        migrations.RemoveField(model_name="blog", name="likes",),
        migrations.AlterField(
            model_name="blog",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 10, 16, 18, 47, 24, 899148),
                editable=False,
            ),
        ),
        migrations.CreateModel(
            name="Like",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "blog",
                    models.ForeignKey(
                        default="",
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="blogs.blog",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default="",
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
