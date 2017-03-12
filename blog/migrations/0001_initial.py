# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=5000)),
                ('body', models.TextField()),
                ('date', models.DateField(default=datetime.datetime(2017, 3, 12, 10, 23, 59, 161468))),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
                ('date', models.DateField(default=datetime.datetime(2017, 3, 12, 10, 23, 59, 162178))),
                ('blog', models.ForeignKey(blank=True, to='blog.blog', null=True)),
            ],
        ),
    ]
