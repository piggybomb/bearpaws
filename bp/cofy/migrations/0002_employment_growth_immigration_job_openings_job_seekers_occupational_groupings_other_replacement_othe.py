# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cofy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='employment_growth',
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
        migrations.CreateModel(
            name='immigration',
            fields=[
                ('noc', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('y2012', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2013', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2014', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2015', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2016', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2017', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2018', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2019', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2020', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2021', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2022', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='job_openings',
            fields=[
                ('noc', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('y2012', models.DecimalField(default=0, max_digits=9, decimal_places=6)),
                ('y2013', models.DecimalField(default=0, max_digits=9, decimal_places=6)),
                ('y2014', models.DecimalField(default=0, max_digits=9, decimal_places=6)),
                ('y2015', models.DecimalField(default=0, max_digits=9, decimal_places=6)),
                ('y2016', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2017', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2018', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2019', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2020', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2021', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2022', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='job_seekers',
            fields=[
                ('noc', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('y2012', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2013', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2014', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2015', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2016', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2017', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2018', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2019', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2020', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2021', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2022', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='occupational_groupings',
            fields=[
                ('noc', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('occupational_grouping', models.CharField(max_length=194)),
                ('occupation', models.CharField(max_length=420)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='other_replacement',
            fields=[
                ('noc', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('y2012', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2013', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2014', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2015', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2016', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2017', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2018', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2019', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2020', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2021', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2022', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='other_seekers',
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
        migrations.CreateModel(
            name='retirements',
            fields=[
                ('noc', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('y2012', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2013', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2014', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2015', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2016', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2017', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2018', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2019', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2020', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2021', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2022', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='school_leavers',
            fields=[
                ('noc', models.CharField(max_length=5, serialize=False, primary_key=True)),
                ('y2012', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2013', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2014', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2015', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2016', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2017', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2018', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2019', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2020', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2021', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
                ('y2022', models.DecimalField(default=0, max_digits=8, decimal_places=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='summary',
            fields=[
                ('noc', models.CharField(max_length=5, primary_key=True)),
                ('employment_in_2012', models.DecimalField(default=0, max_digits=5, decimal_places=1)),
                ('employment_growth_2013_2022', models.DecimalField(default=0, max_digits=5, decimal_places=1)),
                ('retirements_2013_2022', models.DecimalField(default=0, max_digits=4, decimal_places=1)),
                ('other_replacement_2013_2022', models.DecimalField(default=0, max_digits=4, decimal_places=1)),
                ('job_openings_2013_2022', models.DecimalField(default=0, max_digits=5, decimal_places=1)),
                ('school_leavers_2013_2022', models.DecimalField(default=0, max_digits=5, decimal_places=1)),
                ('immigrants_2013_2022', models.DecimalField(default=0, max_digits=4, decimal_places=1)),
                ('job_seekers_2013_other_2013_2022', models.DecimalField(default=0, max_digits=5, decimal_places=1)),
                ('job_seekers_all_2013_2022', models.DecimalField(default=0, max_digits=5, decimal_places=1)),
                ('labour_market_conditions_2010_2012', models.CharField(max_length=8)),
                ('projected_labour_market_conditions_2013_2022', models.CharField(max_length=5, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
