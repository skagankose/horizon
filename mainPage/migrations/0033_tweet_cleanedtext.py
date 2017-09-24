# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0032_auto_20170605_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='cleanedText',
            field=models.TextField(default=''),
        ),
    ]
