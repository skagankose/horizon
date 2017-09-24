# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0030_auto_20170605_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='createdDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
