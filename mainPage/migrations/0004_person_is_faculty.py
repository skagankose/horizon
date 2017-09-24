# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0003_remove_person_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='is_faculty',
            field=models.BooleanField(default=b'False'),
        ),
    ]
