# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_idioma_eintrousername'),
    ]

    operations = [
        migrations.AddField(
            model_name='idioma',
            name='actualizar',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
