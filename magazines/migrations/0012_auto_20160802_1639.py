# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 16:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0011_auto_20160801_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 2, 16, 39, 4, 310229, tzinfo=utc)),
        ),
    ]
