# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0034_auto_20170611_0131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twitteraccount',
            name='relatedPerson',
        ),
        migrations.DeleteModel(
            name='CustomPerson',
        ),
    ]
