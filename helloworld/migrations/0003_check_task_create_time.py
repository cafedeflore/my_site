# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0002_auto_20150423_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='check_task',
            name='create_time',
            field=models.DateTimeField(default=-28800),
        ),
    ]
