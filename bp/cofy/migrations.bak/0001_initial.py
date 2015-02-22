# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employment',
            fields=[
                ('noc', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('y2012', models.DecimalField(default=0, max_digits=9, decimal_places=6)),
                ('y2013', models.DecimalField(default=0, max_digits=9, decimal_places=6)),
                ('y2014', models.DecimalField(default=0, max_digits=9, decimal_places=6)),
                ('y2015', models.DecimalField(default=0, max_digits=9, decimal_places=6)),
                ('y2016', models.DecimalField(default=0, max_digits=9, decimal_places=6)),
                ('y2017', models.DecimalField(default=0, max_digits=9, decimal_places=6)),
                ('y2018', models.DecimalField(default=0, max_digits=9, decimal_places=6)),
                ('y2019', models.DecimalField(default=0, max_digits=9, decimal_places=6)),
                ('y2020', models.DecimalField(default=0, max_digits=9, decimal_places=6)),
                ('y2021', models.DecimalField(default=0, max_digits=9, decimal_places=6)),
                ('y2022', models.DecimalField(default=0, max_digits=9, decimal_places=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
