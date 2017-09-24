# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0006_auto_20160314_0834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generaltext',
            name='author_name',
        ),
        migrations.RemoveField(
            model_name='generaltext',
            name='slug2',
        ),
        migrations.AddField(
            model_name='person',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
