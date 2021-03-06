# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-08-25 00:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=250)),
                ('capacity', models.IntegerField()),
                ('schedule', models.DateField(default=django.utils.timezone.now)),
                ('reservation_status', models.CharField(choices=[('ND', 'No Disponible'), ('D', 'Disponible'), ('R', 'Reservada'), ('C', 'Confirmada')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date', models.DateField(default=django.utils.timezone.now)),
                ('from_date', models.DateField(default=django.utils.timezone.now)),
                ('to_date', models.DateField(default=django.utils.timezone.now)),
                ('assistants', models.IntegerField(default=0)),
                ('supplies_quantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ReservationRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField(default=django.utils.timezone.now)),
                ('approved', models.NullBooleanField()),
            ],
        ),
    ]
