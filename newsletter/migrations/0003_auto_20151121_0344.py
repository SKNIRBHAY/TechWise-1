# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20151115_1402'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='first_name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='last_name',
        ),
    ]
