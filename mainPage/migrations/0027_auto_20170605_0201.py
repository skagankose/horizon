# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0026_twitteraccount_profilebanner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='twitteraccount',
            options={'ordering': ('-pk',)},
        ),
        migrations.AddField(
            model_name='tweet',
            name='coordinates',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='tweet',
            name='country',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AddField(
            model_name='tweet',
            name='countryCode',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AddField(
            model_name='tweet',
            name='countryFull',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AddField(
            model_name='tweet',
            name='createdDate',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='tweet',
            name='hashtags',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='tweet',
            name='language',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='tweet',
            name='liked',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tweet',
            name='mentions',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='tweet',
            name='placeID',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tweet',
            name='placeType',
            field=models.CharField(max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='tweet',
            name='quoteTweetID',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tweet',
            name='replyTweetID',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tweet',
            name='replyUserID',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tweet',
            name='retweetTweetID',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tweet',
            name='retweets',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tweet',
            name='tweetID',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tweet',
            name='urls',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
