# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cofy', '0003_auto_20150222_0023'),
    ]

    operations = [
        migrations.CreateModel(
            name='test_table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('noc', models.CharField(max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
