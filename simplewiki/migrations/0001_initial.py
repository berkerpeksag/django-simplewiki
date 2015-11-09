# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('is_published', models.BooleanField(verbose_name='Publish?', default=True)),
                ('is_locked', models.BooleanField(verbose_name='Locked to edits?', default=False)),
                ('content', models.TextField(verbose_name='Content')),
                ('rendered', models.TextField(blank=True, editable=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
                'ordering': ('-updated_on',),
                'permissions': [('can_lock', 'Can lock a document to edits')],
            },
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('content', models.TextField(verbose_name='Content')),
                ('rendered', models.TextField(blank=True, editable=False)),
                ('diff', models.TextField(blank=True, editable=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True)),
                ('document', models.ForeignKey(related_name='revisions', to='simplewiki.Document')),
            ],
            options={
                'ordering': ('-created_on',),
                'get_latest_by': 'created_on',
            },
        ),
    ]
