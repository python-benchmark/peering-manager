# Generated by Django 2.1.4 on 2018-12-12 20:06

from django.db import migrations, models


class Migration(migrations.Migration):
    def forwards_func(apps, schema_editor):
        Network = apps.get_model("peeringdb", "Network")
        db_alias = schema_editor.connection.alias
        Network.objects.using(db_alias).filter(info_prefixes4=None).update(
            info_prefixes4=0
        )
        Network.objects.using(db_alias).filter(info_prefixes6=None).update(
            info_prefixes6=0
        )

    def reverse_func(apps, schema_editor):
        Network = apps.get_model("peeringdb", "Network")
        db_alias = schema_editor.connection.alias
        Network.objects.using(db_alias).filter(info_prefixes4=0).update(
            info_prefixes4=None
        )
        Network.objects.using(db_alias).filter(info_prefixes6=0).update(
            info_prefixes6=None
        )

    dependencies = [("peeringdb", "0007_peerrecord")]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
        migrations.AlterField(
            model_name="network",
            name="info_prefixes4",
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="network",
            name="info_prefixes6",
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
