# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 17:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MyBlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 24, 17, 6, 42, 469735, tzinfo=utc)),
        ),
    ]
