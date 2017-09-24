# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0027_auto_20170605_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='coordinates',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
