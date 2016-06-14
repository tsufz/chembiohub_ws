# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-13 10:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cbh_core_model', '0052_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='skinningconfig',
            name='maintenance_warning',
            field=models.NullBooleanField(default=False, help_text=b'Whether a maintenance warning should be displayed'),
        ),
        migrations.AddField(
            model_name='skinningconfig',
            name='maintenance_warning_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 13, 10, 0, 39, 712355, tzinfo=utc), help_text=b'The end time of the maintenance warning message'),
        ),
        migrations.AddField(
            model_name='skinningconfig',
            name='maintenance_warning_message',
            field=models.CharField(default=b'', help_text=b'Message to show users to warn them of upcoming maintenance', max_length=300),
        ),
        migrations.AddField(
            model_name='skinningconfig',
            name='maintenance_warning_start',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 13, 10, 0, 39, 712322, tzinfo=utc), help_text=b'The start time of the maintenance warning message'),
        ),
    ]