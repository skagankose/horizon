# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0035_auto_20170611_0133'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomPerson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('fullName', models.CharField(default='', max_length=200)),
                ('avatar', models.ImageField(blank=True, upload_to='mainPage/static/img/', null=True)),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatedDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='twitteraccount',
            name='relatedPerson',
            field=models.ForeignKey(blank=True, null=True, to='mainPage.CustomPerson', related_name='twitterAccount'),
        ),
    ]
