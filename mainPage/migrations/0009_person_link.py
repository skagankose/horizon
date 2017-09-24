# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0008_auto_20170209_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='link',
            field=models.TextField(default='/people'),
        ),
    ]
