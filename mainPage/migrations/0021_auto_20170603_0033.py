# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0020_tweet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='realtedAccount',
            new_name='relatedAccount',
        ),
        migrations.RenameField(
            model_name='twitteraccount',
            old_name='realtedPerson',
            new_name='relatedPerson',
        ),
        migrations.RemoveField(
            model_name='twitteraccount',
            name='country',
        ),
    ]
