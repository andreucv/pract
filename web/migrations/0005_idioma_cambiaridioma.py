# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20150121_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='idioma',
            name='cambiaridioma',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
    ]
