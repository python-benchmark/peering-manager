# Generated by Django 2.1.2 on 2018-10-14 14:12

import django.db.models.deletion
from django.db import migrations, models

import peering.fields


class Migration(migrations.Migration):
    dependencies = [("peering", "0017_auto_20180802_2309")]

    operations = [
        migrations.CreateModel(
            name="DirectPeeringSession",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("ip_address", models.GenericIPAddressField()),
                ("password", models.CharField(blank=True, max_length=255, null=True)),
                ("enabled", models.BooleanField(default=True)),
                (
                    "bgp_state",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("idle", "Idle"),
                            ("connect", "Connect"),
                            ("active", "Active"),
                            ("opensent", "OpenSent"),
                            ("openconfirm", "OpenConfirm"),
                            ("established", "Established"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "received_prefix_count",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                (
                    "advertised_prefix_count",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                ("comment", models.TextField(blank=True)),
                ("local_asn", peering.fields.ASNField(default=0)),
                (
                    "relationship",
                    models.CharField(
                        choices=[
                            ("private-peering", "Private Peering"),
                            ("transit-provider", "Transit Provider"),
                            ("customer", "Customer"),
                        ],
                        help_text="Relationship with the remote peer.",
                        max_length=50,
                    ),
                ),
                (
                    "autonomous_system",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="peering.AutonomousSystem",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.RenameModel(
            old_name="PeeringSession", new_name="InternetExchangePeeringSession"
        ),
    ]