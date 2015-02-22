# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cofy', '0002_employment_growth_immigration_job_openings_job_seekers_occupational_groupings_other_replacement_othe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary',
            name='noc',
            field=models.CharField(max_length=5, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='summary',
            name='projected_labour_market_conditions_2013_2022',
            field=models.CharField(max_length=8),
            preserve_default=True,
        ),
    ]
