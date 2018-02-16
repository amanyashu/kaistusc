# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-02-16 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='role',
            field=models.CharField(choices=[('DEFAULT', '기본'), ('PROJECT', '사업'), ('DEBATE', '논의')], default='DEFAULT', max_length=32, verbose_name='보드 역할'),
        ),
    ]
