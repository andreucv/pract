# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_idioma_comentariohora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idioma',
            name='eIntroEmail',
        ),
        migrations.RemoveField(
            model_name='idioma',
            name='eIntroFirst_name',
        ),
        migrations.RemoveField(
            model_name='idioma',
            name='eIntroLast_name',
        ),
        migrations.RemoveField(
            model_name='idioma',
            name='eIntroPassword',
        ),
        migrations.RemoveField(
            model_name='idioma',
            name='eIntroUsername',
        ),
        migrations.AddField(
            model_name='idioma',
            name='emailTicketEstado',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idioma',
            name='emailTicketId',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idioma',
            name='emailTicketModificado',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
