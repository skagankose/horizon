# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0025_auto_20170603_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitteraccount',
            name='profileBanner',
            field=models.CharField(max_length=300, default=''),
        ),
    ]
