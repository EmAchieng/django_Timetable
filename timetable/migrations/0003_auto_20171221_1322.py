# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 04:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_auto_20171221_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moduledefinition',
            name='credits',
        ),
        migrations.RemoveField(
            model_name='moduledefinition',
            name='level',
        ),
    ]