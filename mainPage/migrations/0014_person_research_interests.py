# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0013_auto_20170209_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='research_interests',
            field=models.CharField(max_length=200, default=''),
        ),
    ]
