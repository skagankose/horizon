# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0004_person_is_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='is_adjunct',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='is_alumni',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='is_graduate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='is_undergraduate',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='is_faculty',
            field=models.BooleanField(default=False),
        ),
    ]
