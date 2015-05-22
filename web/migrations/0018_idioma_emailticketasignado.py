# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_auto_20150131_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='idioma',
            name='emailTicketAsignado',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
