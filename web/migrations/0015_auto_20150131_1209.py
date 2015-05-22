# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_auto_20150130_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idioma',
            name='cuerpoEmailPost',
        ),
        migrations.RemoveField(
            model_name='idioma',
            name='cuerpoEmailRegistro',
        ),
        migrations.AddField(
            model_name='idioma',
            name='emailNombreCompleto',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idioma',
            name='emailNombreUsuario',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idioma',
            name='emailSr',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idioma',
            name='graciasEmailRegistro',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
