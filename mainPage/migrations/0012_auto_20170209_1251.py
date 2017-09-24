# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0011_auto_20170209_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='text',
            field=models.CharField(choices=[('Twitter', 'Twitter'), ('Google Scholar', 'Google Scholar'), ('Linkedin', 'Linkedin')], max_length=50, null=True),
        ),
    ]
