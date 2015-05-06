# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0005_auto_20150426_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check_task',
            name='create_time',
            field=models.DateTimeField(default=b''),
        ),
    ]
