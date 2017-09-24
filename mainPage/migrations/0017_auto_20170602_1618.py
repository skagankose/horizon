# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0016_auto_20170313_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='activityimage',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='generaltext',
            name='author',
        ),
        migrations.DeleteModel(
            name='Presentation',
        ),
        migrations.RemoveField(
            model_name='project',
            name='author',
        ),
        migrations.RemoveField(
            model_name='project',
            name='contributers',
        ),
        migrations.RemoveField(
            model_name='project',
            name='funders',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='links',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='published_in',
        ),
        migrations.DeleteModel(
            name='Slide',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='fullName',
        ),
        migrations.RemoveField(
            model_name='person',
            name='description',
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_adjunct',
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_alumni',
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_faculty',
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_graduate',
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_joint',
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_supporter',
        ),
        migrations.RemoveField(
            model_name='person',
            name='is_undergraduate',
        ),
        migrations.RemoveField(
            model_name='person',
            name='link',
        ),
        migrations.RemoveField(
            model_name='person',
            name='research_interests',
        ),
        migrations.AddField(
            model_name='person',
            name='userName',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
        migrations.DeleteModel(
            name='ActivityImage',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='GeneralText',
        ),
        migrations.DeleteModel(
            name='Link',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
        migrations.AddField(
            model_name='tweet',
            name='person',
            field=models.ForeignKey(to='mainPage.Person'),
        ),
    ]
