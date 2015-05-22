# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0021_idioma_nuevocomentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='idioma',
            name='ticketsbuscados',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
