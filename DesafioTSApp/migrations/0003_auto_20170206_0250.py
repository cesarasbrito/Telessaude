# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('DesafioTSApp', '0002_solicitacao_datasolicitacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='DataSolicitacao',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 6, 4, 50, 11, 93620, tzinfo=utc)),
        ),
    ]
