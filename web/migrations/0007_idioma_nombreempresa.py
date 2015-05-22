# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20150124_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='idioma',
            name='nombreempresa',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
