# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0015_auto_20170209_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('slideImage', models.ImageField(upload_to='mainPage/static/img/', null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='text',
            field=models.CharField(max_length=50, choices=[('Github', 'Github'), ('Twitter', 'Twitter'), ('Google Scholar', 'Google Scholar'), ('Linkedin', 'Linkedin')], null=True),
        ),
    ]
