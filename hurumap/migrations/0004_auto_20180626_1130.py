# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-26 08:30
from __future__ import unicode_literals

import datetime
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wazimap', '0008_auto_20170424_1209'),
        ('hurumap', '0003_auto_20180616_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataindicatorvalue',
            name='country',
        ),
        migrations.RemoveField(
            model_name='dataindicatorvalue',
            name='date',
        ),
        migrations.RemoveField(
            model_name='dataindicatorvalue',
            name='decimal',
        ),
        migrations.RemoveField(
            model_name='dataindicatorvalue',
            name='geo',
        ),
        migrations.RemoveField(
            model_name='dataindicatorvalue',
            name='indicator',
        ),
        migrations.RemoveField(
            model_name='dataindicatorvalue',
            name='publisher_data',
        ),
        migrations.RemoveField(
            model_name='dataindicatorvalue',
            name='value',
        ),
        migrations.AddField(
            model_name='dataindicator',
            name='country',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=b''),
        ),
        migrations.AddField(
            model_name='dataindicator',
            name='date',
            field=models.CharField(default=datetime.datetime(2018, 6, 26, 8, 30, 28, 412845, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dataindicator',
            name='decimal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dataindicator',
            name='geo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wazimap.Geography'),
        ),
        migrations.AddField(
            model_name='dataindicator',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=36, null=True),
        ),
    ]