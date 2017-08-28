# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-08-28 11:50
from __future__ import unicode_literals

from django.db import migrations, models
import meetings.models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0006_auto_20170827_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='requested_supplies',
            field=models.ManyToManyField(through='meetings.SupplyDetail', to='meetings.Supply'),
        ),
        migrations.AlterField(
            model_name='meetingroom',
            name='supplies',
            field=models.ManyToManyField(blank=True, default=meetings.models.MeetingRoom.default_supplies, to='meetings.Supply'),
        ),
    ]
