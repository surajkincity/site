# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170312_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 3, 12, 14, 56, 53, 831088)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.CharField(max_length=5000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 3, 12, 14, 56, 53, 831830)),
        ),
    ]
