# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0010_person_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='text',
            field=models.CharField(null=True, max_length=50, choices=[('Twitter', 'Twitter'), ('Google Scholar', 'Google Scholar'), ('Linkedin', 'Linkedin'), ('Anadolu İmam Hatip', 'Anadolu İmam Hatip')]),
        ),
    ]
