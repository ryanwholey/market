# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venue',
            old_name='capactity',
            new_name='capacity',
        ),
    ]
