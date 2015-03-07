# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11, null=True, blank=True)),
                ('address', models.CharField(max_length=30, null=True, blank=True)),
                ('neighborhood', models.CharField(max_length=20, null=True, blank=True)),
                ('city', models.CharField(max_length=20, null=True, blank=True)),
                ('state', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
    ]
