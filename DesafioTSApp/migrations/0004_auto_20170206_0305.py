# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('DesafioTSApp', '0003_auto_20170206_0250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitante',
            name='id',
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='DataSolicitacao',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 6, 5, 5, 10, 554596, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='solicitante',
            name='CPF',
            field=models.TextField(primary_key=True, max_length=14, serialize=False),
        ),
    ]
