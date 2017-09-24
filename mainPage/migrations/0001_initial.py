# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('webpage', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200)),
                ('link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('adress', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=200)),
                ('title', models.CharField(default=b'None', max_length=200)),
                ('avatar', models.ImageField(null=True, upload_to=b'mainPage/static/img/', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('main_file', models.FileField(null=True, upload_to=b'mainPage/static/file/', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(related_name='projects_owned', blank=True, to='mainPage.Person', null=True)),
                ('contributers', models.ManyToManyField(related_name='projects_contributed', to='mainPage.Person', blank=True)),
                ('funders', models.ManyToManyField(related_name='projects_funded', to='mainPage.Person', blank=True)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('date', models.CharField(default=b'2016', max_length=100)),
                ('authors', models.ManyToManyField(related_name='publications_owned', to='mainPage.Person', blank=True)),
                ('links', models.ManyToManyField(related_name='publications', to='mainPage.Link', blank=True)),
                ('published_in', models.ForeignKey(related_name='publications_published', blank=True, to='mainPage.Person', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='owner',
            field=models.ForeignKey(related_name='contacts', to='mainPage.Person'),
        ),
    ]
