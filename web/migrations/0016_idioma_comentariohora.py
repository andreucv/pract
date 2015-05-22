# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_auto_20150131_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='idioma',
            name='comentarioHora',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
