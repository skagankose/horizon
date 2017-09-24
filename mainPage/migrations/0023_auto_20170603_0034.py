# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0022_auto_20170603_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='relatedAccount',
            field=models.ForeignKey(blank=True, related_name='tweets', null=True, to='mainPage.TwitterAccount'),
        ),
        migrations.AlterField(
            model_name='twitteraccount',
            name='relatedPerson',
            field=models.ForeignKey(blank=True, related_name='twitterAccount', null=True, to='mainPage.Person'),
        ),
    ]
