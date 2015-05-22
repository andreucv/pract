# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_idioma'),
    ]

    operations = [
        migrations.AddField(
            model_name='idioma',
            name='ticketsasignados',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idioma',
            name='ticketscreados',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
    ]
