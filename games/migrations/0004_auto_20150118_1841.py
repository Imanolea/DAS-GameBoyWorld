# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_game_imageurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='downloadurl',
            field=models.URLField(default=datetime.datetime(2015, 1, 18, 17, 41, 9, 129911, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='ingameurl',
            field=models.URLField(default=datetime.datetime(2015, 1, 18, 17, 41, 17, 700402, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
