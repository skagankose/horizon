# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0033_tweet_cleanedtext'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomPerson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('fullName', models.CharField(max_length=200, default='')),
                ('avatar', models.ImageField(upload_to='mainPage/static/img/', null=True, blank=True)),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatedDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AlterField(
            model_name='twitteraccount',
            name='relatedPerson',
            field=models.ForeignKey(null=True, blank=True, to='mainPage.CustomPerson', related_name='twitterAccount'),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
