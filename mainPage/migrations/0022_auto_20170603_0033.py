# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0021_auto_20170603_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='relatedAccount',
            field=models.ForeignKey(to='mainPage.TwitterAccount', related_name='tweets', blank=True),
        ),
        migrations.AlterField(
            model_name='twitteraccount',
            name='relatedPerson',
            field=models.ForeignKey(to='mainPage.Person', related_name='twitterAccount', blank=True),
        ),
    ]
