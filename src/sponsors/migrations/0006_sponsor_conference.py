# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-02 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0005_auto_20160530_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='conference',
            field=models.SlugField(choices=[('pycontw-2016', 'PyCon Taiwan 2016'), ('pycontw-2017', 'PyCon Taiwan 2017')], default='pycontw-2017', verbose_name='conference'),
        ),
    ]
