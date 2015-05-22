# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_idioma_cambiaridioma'),
    ]

    operations = [
        migrations.AddField(
            model_name='idioma',
            name='bienvenida',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idioma',
            name='subbienvenida',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
