# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-12 13:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0022_auto_20160812_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 12, 13, 19, 30, 207243, tzinfo=utc)),
        ),
    ]
