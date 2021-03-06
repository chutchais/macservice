# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 07:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0004_auto_20161001_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(blank=True, max_length=200, null=True)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='bom',
            options={'ordering': ['product']},
        ),
        migrations.AddField(
            model_name='inventory',
            name='bom_part',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inv_list', to='shop.Bom'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='receiving',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receive_inv_list', to='shop.Receiving_detail'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
