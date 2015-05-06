# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0007_auto_20150426_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check_task',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime),
        ),
    ]
