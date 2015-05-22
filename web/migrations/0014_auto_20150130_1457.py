# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_idioma_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='idioma',
            name='cuerpoEmailPost',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idioma',
            name='cuerpoEmailRegistro',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idioma',
            name='tituloEmailPost',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idioma',
            name='tituloEmailRegistro',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
