# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 11:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name=b'creator name')),
                ('profile_url', models.URLField(verbose_name=b'creator profile')),
            ],
        ),
        migrations.CreateModel(
            name='Prezi',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name=b'id')),
                ('title', models.CharField(max_length=200, verbose_name=b'title')),
                ('thumbnail', models.URLField(verbose_name=b'thumbnail')),
                ('created_on', models.DateField(blank=True, null=True, verbose_name=b'created on')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prezis', to='prezi.Creator', verbose_name=b'creator')),
            ],
        ),
    ]
