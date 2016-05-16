# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-04 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cbh_core_model', '0046_auto_20160504_0945'),
        ('cbh_chembl_model_extension', '0035_auto_20160504_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='cbhcompoundmultiplebatch',
            name='uploaded_file',
            field=models.ForeignKey(blank=True, default=None, help_text=b'File that was uploaded to generate this multiple batch', null=True, on_delete=django.db.models.deletion.CASCADE, to='cbh_core_model.CBHFlowFile'),
        ),
    ]
