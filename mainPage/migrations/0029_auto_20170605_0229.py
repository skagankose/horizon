# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0028_auto_20170605_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='replyTweetID',
            field=models.IntegerField(default=0, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='retweetTweetID',
            field=models.IntegerField(default=0, blank=True, null=True),
        ),
    ]
