# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-10 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hurumap', '0004_auto_20180609_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataindicator',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='dataindicator',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
