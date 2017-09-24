# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0018_auto_20170602_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('userID', models.IntegerField(default=0)),
                ('screenName', models.CharField(default='', max_length=200)),
                ('fullName', models.CharField(default='', max_length=200)),
                ('joined', models.CharField(default='', max_length=200)),
                ('description', models.TextField()),
                ('url', models.TextField()),
                ('likeCount', models.IntegerField(default=0)),
                ('followersCount', models.IntegerField(default=0)),
                ('followeeCount', models.IntegerField(default=0)),
                ('language', models.CharField(default='', max_length=50)),
                ('listedCount', models.IntegerField(default=0)),
                ('location', models.CharField(default='', max_length=50)),
                ('twitterCount', models.IntegerField(default=0)),
                ('timeZone', models.CharField(default='', max_length=50)),
                ('country', models.CharField(default='', max_length=50)),
                ('profileBackground', models.ImageField(null=True, upload_to='mainPage/static/img/', blank=True)),
                ('profileImage', models.ImageField(null=True, upload_to='mainPage/static/img/', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='person',
        ),
        migrations.RemoveField(
            model_name='person',
            name='userName',
        ),
        migrations.AddField(
            model_name='person',
            name='createdDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='person',
            name='updatedDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='Tweet',
        ),
        migrations.AddField(
            model_name='twitteraccount',
            name='realtedPerson',
            field=models.ForeignKey(to='mainPage.Person', related_name='twitterAccount'),
        ),
    ]
