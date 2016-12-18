# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 20:01
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('symbol', models.CharField(max_length=4)),
                ('buy', models.PositiveIntegerField(default=1000000)),
                ('sell', models.PositiveIntegerField(default=1000000)),
                ('stock_price', models.FloatField(default=1000.0)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_text', models.CharField(max_length=500)),
                ('impact1', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(-5)])),
                ('impact2', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(-5)])),
                ('impact3', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(-5)])),
                ('impact4', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(-5)])),
                ('impact5', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(-5)])),
                ('impact6', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(-5)])),
                ('impact7', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(-5)])),
                ('impact8', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(-5)])),
                ('impact9', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(-5)])),
                ('impact10', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(-5)])),
                ('quick_iter', models.PositiveIntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='NewsPublished',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_text', models.CharField(max_length=500)),
                ('impact1', models.IntegerField(default=0)),
                ('impact2', models.IntegerField(default=0)),
                ('impact3', models.IntegerField(default=0)),
                ('impact4', models.IntegerField(default=0)),
                ('impact5', models.IntegerField(default=0)),
                ('impact6', models.IntegerField(default=0)),
                ('impact7', models.IntegerField(default=0)),
                ('impact8', models.IntegerField(default=0)),
                ('impact9', models.IntegerField(default=0)),
                ('impact10', models.IntegerField(default=0)),
                ('quick_iter', models.PositiveIntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('iteration_counter', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'News Published',
                'verbose_name_plural': 'News Published',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('stock_price', models.FloatField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockmarket.Company')),
            ],
        ),
    ]