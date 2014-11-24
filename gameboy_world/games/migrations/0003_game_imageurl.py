# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_game_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='imageurl',
            field=models.URLField(default=datetime.datetime(2014, 11, 24, 17, 6, 10, 550762, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
