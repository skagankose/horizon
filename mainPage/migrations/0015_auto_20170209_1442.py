# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0014_person_research_interests'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityImage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('image', models.ImageField(null=True, blank=True, upload_to='mainPage/static/activityimg/')),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='description',
            field=models.CharField(max_length=10000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='title',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='webpage',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='description',
            field=models.CharField(max_length=700, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='research_interests',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='activityimage',
            name='activity',
            field=models.ForeignKey(to='mainPage.Activity', related_name='images'),
        ),
    ]
