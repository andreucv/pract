# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechahora', models.DateTimeField()),
                ('texto', models.CharField(max_length=500)),
                ('tecnico', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=10)),
                ('numero', models.IntegerField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Prioridad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=10)),
                ('numero', models.IntegerField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texto', models.CharField(max_length=500)),
                ('fechahora', models.DateTimeField()),
                ('asignado', models.ForeignKey(related_name='asignado', to=settings.AUTH_USER_MODEL)),
                ('comentarios', models.ManyToManyField(to='web.Comentario')),
                ('creador', models.ForeignKey(related_name='creador', to=settings.AUTH_USER_MODEL)),
                ('estado', models.ForeignKey(to='web.Estado')),
                ('prioridad', models.ForeignKey(to='web.Prioridad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
