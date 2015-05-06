# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0004_auto_20150426_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check_task',
            name='create_time',
            field=models.DateTimeField(default=b'1980-00-00 00:00:00'),
        ),
    ]
