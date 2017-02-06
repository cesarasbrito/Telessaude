# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Texto', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Nome', models.TextField(max_length=150)),
                ('Email', models.EmailField(max_length=65)),
                ('Telefone', models.TextField(max_length=30)),
                ('CPF', models.TextField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Teleconsultor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('Nome', models.TextField(max_length=150)),
                ('Email', models.EmailField(max_length=65)),
                ('CRM', models.TextField(max_length=10)),
                ('DataFormatura', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='solicitacao',
            name='solicitante',
            field=models.ForeignKey(to='DesafioTSApp.Solicitante'),
        ),
    ]
