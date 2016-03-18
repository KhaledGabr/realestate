# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 01:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_title', models.CharField(max_length=200)),
                ('property_description', models.TextField(max_length=1000)),
                ('property_address', models.CharField(max_length=300)),
                ('property_price', models.IntegerField()),
                ('property_owner_name', models.CharField(max_length=200)),
                ('property_owner_phone', models.CharField(max_length=30)),
                ('property_owner_comments', models.CharField(max_length=200)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]