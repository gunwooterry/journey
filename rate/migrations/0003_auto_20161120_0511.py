# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-20 05:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0002_auto_20161117_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_id', models.PositiveSmallIntegerField()),
                ('tag_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='destination',
            name='tag1',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='tag2',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='tag3',
        ),
        migrations.AddField(
            model_name='destination',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rate.Country'),
        ),
        migrations.AddField(
            model_name='destination',
            name='tag1',
            field=models.ManyToManyField(related_name='_destination_tag1_+', to='rate.Tag'),
        ),
        migrations.AddField(
            model_name='destination',
            name='tag2',
            field=models.ManyToManyField(related_name='_destination_tag2_+', to='rate.Tag'),
        ),
        migrations.AddField(
            model_name='destination',
            name='tag3',
            field=models.ManyToManyField(related_name='_destination_tag3_+', to='rate.Tag'),
        ),
    ]
