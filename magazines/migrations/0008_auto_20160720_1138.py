# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 11:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0007_auto_20160720_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 20, 11, 38, 32, 155807, tzinfo=utc)),
        ),
    ]