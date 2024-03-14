# Generated by Django 2.2.1 on 2019-05-09 21:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("peering", "0042_auto_20190509_1439")]

    operations = [
        migrations.AddField(
            model_name="router",
            name="use_netbox",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="Use NetBox to communicate instead of NAPALM",
            ),
        )
    ]
