# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0029_auto_20170605_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='replyUserID',
            field=models.IntegerField(null=True, default=0, blank=True),
        ),
    ]
