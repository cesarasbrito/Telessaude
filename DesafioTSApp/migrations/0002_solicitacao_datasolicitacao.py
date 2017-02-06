# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DesafioTSApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacao',
            name='DataSolicitacao',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
