# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-16 16:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbh_core_model', '0046_auto_20160504_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customfieldconfig',
            name='data_type',
        ),
        migrations.RemoveField(
            model_name='pinnedcustomfield',
            name='part_of_blinded_key',
        ),
        migrations.RemoveField(
            model_name='pinnedcustomfield',
            name='pinned_for_datatype',
        ),
        migrations.RemoveField(
            model_name='project',
            name='is_default',
        ),
        migrations.DeleteModel(
            name='DataType',
        ),
    ]
