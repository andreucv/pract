# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_idioma_actualizar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estado',
            name='numero',
        ),
        migrations.RemoveField(
            model_name='prioridad',
            name='numero',
        ),
        migrations.AddField(
            model_name='idioma',
            name='asignar',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idioma',
            name='estado',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idioma',
            name='prioridad',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
