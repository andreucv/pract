# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_idioma_nombreempresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='idioma',
            name='eYaExisteUsuario',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idioma',
            name='email',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
