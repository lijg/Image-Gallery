# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-23 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250)),
                ('original', models.ImageField(default='/tmp/none.jpg', upload_to=b'uploads')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
