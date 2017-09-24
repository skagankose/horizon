# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0023_auto_20170603_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitteraccount',
            name='profileBackground',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AlterField(
            model_name='twitteraccount',
            name='profileImage',
            field=models.CharField(max_length=50, default=''),
        ),
    ]
