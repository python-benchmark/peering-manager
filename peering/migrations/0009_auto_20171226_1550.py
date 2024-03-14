# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-26 14:50


from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("peering", "0008_auto_20171212_2251")]

    operations = [
        migrations.RemoveField(model_name="autonomoussystem", name="ipv4_as_set"),
        migrations.RemoveField(model_name="autonomoussystem", name="ipv6_as_set"),
        migrations.AddField(
            model_name="autonomoussystem",
            name="irr_as_set",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
