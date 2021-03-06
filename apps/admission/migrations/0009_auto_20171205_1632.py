# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-05 16:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admission', '0008_auto_20171204_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admissionprocess',
            name='department',
        ),
        migrations.RemoveField(
            model_name='admissionprocess',
            name='payment_date',
        ),
        migrations.RemoveField(
            model_name='admissionprocess',
            name='registration_fees_paid',
        ),
        migrations.AddField(
            model_name='admissionprocess',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admissionprocess',
            name='approved_by_commitee',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admissionprocess',
            name='modify_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='admissionprocess',
            name='pass_admission_test',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admissionprocess',
            name='pass_bac',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admissionprocess',
            name='pass_medical_test',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admissionprocess',
            name='registree_number',
            field=models.CharField(default=1, editable=False, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='admissionprocess',
            name='registree',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='process_registree', to='admission.Registration'),
        ),
    ]
