# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20150308_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, related_name='todos'),
            preserve_default=True,
        ),
    ]
