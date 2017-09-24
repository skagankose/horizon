# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0002_auto_20160311_0803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='title',
        ),
    ]
