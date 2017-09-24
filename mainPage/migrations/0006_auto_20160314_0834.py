# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0005_auto_20160311_0818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=200, null=True)),
                ('text', models.TextField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('counter', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author_name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200, null=True)),
                ('text', ckeditor.fields.RichTextField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField()),
                ('slug2', models.SlugField()),
                ('author', models.ForeignKey(blank=True, to='mainPage.Person', null=True)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(related_name='comments', to='mainPage.GeneralText', null=True),
        ),
    ]
