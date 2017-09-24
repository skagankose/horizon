# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0017_auto_20170602_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='person',
            field=models.ForeignKey(related_name='Tweets', to='mainPage.Person'),
        ),
    ]
