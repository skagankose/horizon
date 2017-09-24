# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0024_auto_20170603_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitteraccount',
            name='profileBackground',
            field=models.CharField(max_length=300, default=''),
        ),
        migrations.AlterField(
            model_name='twitteraccount',
            name='profileImage',
            field=models.CharField(max_length=300, default=''),
        ),
    ]
