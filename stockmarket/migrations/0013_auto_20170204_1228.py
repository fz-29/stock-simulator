# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-04 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmarket', '0012_merge_20170203_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='repay_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]