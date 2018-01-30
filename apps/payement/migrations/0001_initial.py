# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-18 17:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0003_auto_20180118_1726'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('fee_value', models.DecimalField(decimal_places=2, max_digits=32)),
                ('fee_description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Payement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payement_date', models.DateField()),
                ('fees', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payement.Fees')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registration_payement', to='student.Student')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
