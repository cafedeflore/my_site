# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='check_task',
            name='checklist',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='check_task',
            name='config_check',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='check_task',
            name='db_compare',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='check_task',
            name='log_monitor',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='check_task',
            name='pause_point_check',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='check_task',
            name='sql_check',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='check_task',
            name='name',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
