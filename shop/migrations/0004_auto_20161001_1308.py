# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20161001_1244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receiving',
            old_name='transport_fee',
            new_name='trans_fee',
        ),
        migrations.RemoveField(
            model_name='receiving',
            name='transporter',
        ),
        migrations.AddField(
            model_name='receiving',
            name='trans_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='receiving',
            name='trans_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='receiving',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
