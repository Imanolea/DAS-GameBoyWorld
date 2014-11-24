# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2014, 11, 24, 12, 2, 51, 92228, tzinfo=utc), unique=True, max_length=200),
            preserve_default=False,
        ),
    ]
