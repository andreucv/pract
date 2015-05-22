# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0022_idioma_ticketsbuscados'),
    ]

    operations = [
        migrations.AddField(
            model_name='idioma',
            name='emailTicketFinalizado',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
