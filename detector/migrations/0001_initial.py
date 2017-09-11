# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-11 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('headline', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='props',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_date', models.DateTimeField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detector.Article')),
            ],
        ),
    ]
