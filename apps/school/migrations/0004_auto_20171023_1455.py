# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-23 14:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_academicyear_school'),
    ]

    operations = [
        migrations.RenameField(
            model_name='academicyear',
            old_name='school',
            new_name='school_name',
        ),
    ]
