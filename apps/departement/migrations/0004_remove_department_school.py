# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-24 11:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departement', '0003_auto_20171024_1008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='school',
        ),
    ]
