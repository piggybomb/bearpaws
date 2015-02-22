# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cofy', '0004_test_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='summary',
            new_name='summary_test',
        ),
    ]
