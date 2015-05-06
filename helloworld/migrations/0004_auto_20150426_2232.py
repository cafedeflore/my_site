# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0003_check_task_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check_task',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
