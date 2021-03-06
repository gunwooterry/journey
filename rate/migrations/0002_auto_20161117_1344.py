# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-17 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='tags',
        ),
        migrations.AddField(
            model_name='destination',
            name='tag1',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='tag2',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='tag3',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='destination',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
