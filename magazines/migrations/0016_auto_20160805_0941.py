# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-05 09:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0015_auto_20160804_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 5, 9, 41, 21, 433935, tzinfo=utc)),
        ),
    ]
