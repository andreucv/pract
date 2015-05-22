# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20150124_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='idioma',
            name='eIntroEmail',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idioma',
            name='eIntroFirst_name',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idioma',
            name='eIntroLast_name',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idioma',
            name='eIntroPassword',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
    ]
