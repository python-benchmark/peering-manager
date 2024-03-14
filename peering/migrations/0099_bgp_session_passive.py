# Generated by Django 4.2.5 on 2023-09-18 16:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("peering", "0098_group_sessions_statuses")]

    operations = [
        migrations.AddField(
            model_name="directpeeringsession",
            name="passive",
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name="internetexchangepeeringsession",
            name="passive",
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
