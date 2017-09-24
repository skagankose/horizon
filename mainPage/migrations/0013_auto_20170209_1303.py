# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0012_auto_20170209_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='description',
            field=models.CharField(default='', max_length=700),
        ),
    ]
