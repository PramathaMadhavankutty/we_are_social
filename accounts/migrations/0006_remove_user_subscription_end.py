# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-05 10:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_subscription_end'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='subscription_end',
        ),
    ]
