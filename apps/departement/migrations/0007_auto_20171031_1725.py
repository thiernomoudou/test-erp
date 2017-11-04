# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-31 17:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departement', '0006_auto_20171030_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cr_code', models.CharField(max_length=6)),
                ('cr_label', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='admission_fees',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classroom',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departement.Department'),
        ),
    ]
