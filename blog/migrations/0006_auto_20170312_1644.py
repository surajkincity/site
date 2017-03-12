# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170312_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 3, 12, 16, 44, 20, 683738)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 3, 12, 16, 44, 20, 684433)),
        ),
    ]
