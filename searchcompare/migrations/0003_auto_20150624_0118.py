# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchcompare', '0002_commentrecord_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentrecord',
            name='comments',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
