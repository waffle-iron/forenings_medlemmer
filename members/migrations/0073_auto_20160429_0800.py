# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-29 06:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0072_auto_20160428_2254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='volunteer',
            options={'verbose_name': 'Frivillig', 'verbose_name_plural': 'Frivillige'},
        ),
    ]
