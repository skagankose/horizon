# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0007_auto_20160315_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='is_joint',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='is_supporter',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='avatar',
            field=models.ImageField(null=True, upload_to='mainPage/static/img/', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=200, default=''),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='main_file',
            field=models.FileField(null=True, upload_to='mainPage/static/file/', blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='date',
            field=models.CharField(max_length=100, default='2016'),
        ),
    ]
