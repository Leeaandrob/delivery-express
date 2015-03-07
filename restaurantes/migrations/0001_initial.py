# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comidas', '0001_initial'),
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pessoas.Person')),
                ('cnpj', models.CharField(max_length=14, null=True, blank=True)),
                ('foods', models.ManyToManyField(to='comidas.Food')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('pessoas.person',),
        ),
    ]
