# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 09:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20170415_1149'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='savedurl',
            unique_together=set([('user', 'url')]),
        ),
    ]
