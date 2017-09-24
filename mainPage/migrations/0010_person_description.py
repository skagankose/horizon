# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0009_person_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='description',
            field=models.CharField(max_length=500, default=''),
        ),
    ]
