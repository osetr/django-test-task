# Generated by Django 3.1.2 on 2020-10-16 17:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blogs', '0003_auto_20201016_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=4024)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 10, 16, 17, 39, 10, 902036), editable=False)),
                ('blog', models.ForeignKey(default='', editable=False, on_delete=django.db.models.deletion.CASCADE, to='blogs.blog')),
            ],
        ),
    ]
