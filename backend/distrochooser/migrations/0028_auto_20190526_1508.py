# Generated by Django 2.1.2 on 2019-05-26 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distrochooser', '0027_auto_20190407_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectionreason',
            name='isNeutralHit',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usersession',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 26, 15, 8, 14, 253203)),
        ),
    ]
