# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_ticket_titulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('idioma', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('titulo', models.CharField(max_length=40)),
                ('registro', models.CharField(max_length=40)),
                ('ayuda', models.CharField(max_length=40)),
                ('nombreusuario', models.CharField(max_length=40)),
                ('contrasena', models.CharField(max_length=40)),
                ('entra', models.CharField(max_length=40)),
                ('confirmaemail', models.CharField(max_length=40)),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('eNoHayTickets', models.CharField(max_length=400)),
                ('nuevaincidencia', models.CharField(max_length=400)),
                ('tituloincidencia', models.CharField(max_length=400)),
                ('cuerpoincidencia', models.CharField(max_length=400)),
                ('enviar', models.CharField(max_length=400)),
                ('salir', models.CharField(max_length=400)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
