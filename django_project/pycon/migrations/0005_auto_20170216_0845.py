# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-16 08:45
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pycon', '0004_merge_20170216_0654'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='conference',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='visit',
            name='conference',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pycon.Conference'),
            preserve_default=False,
        ),
    ]
