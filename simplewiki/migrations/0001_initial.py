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
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='Publish?')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Documents',
                'ordering': ('-updated_on',),
                'verbose_name': 'Document',
            },
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('summary', models.CharField(max_length=100, blank=True)),
                ('content', models.TextField(verbose_name='Content')),
                ('rendered', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('creator_ip', models.GenericIPAddressField(verbose_name='Creator IP')),
                ('creator', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL)),
                ('document', models.ForeignKey(related_name='revisions', to='simplewiki.Document')),
            ],
            options={
                'verbose_name_plural': 'Revisions',
                'get_latest_by': 'created_on',
                'ordering': ('-created_on',),
                'verbose_name': 'Revision',
            },
        ),
    ]
