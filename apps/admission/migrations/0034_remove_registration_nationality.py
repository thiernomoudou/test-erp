# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-17 11:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0033_auto_20180117_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='nationality',
        ),
    ]
