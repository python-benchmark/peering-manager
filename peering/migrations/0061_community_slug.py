# Generated by Django 3.0.8 on 2020-07-19 10:19

from django.db import migrations, models, transaction
from django.utils.text import slugify


class Migration(migrations.Migration):
    dependencies = [("peering", "0060_auto_20200718_0023")]

    @transaction.atomic()
    def set_default_slug(apps, schema_editor):
        Community = apps.get_model("peering", "Community")
        db_alias = schema_editor.connection.alias
        for c in Community.objects.using(db_alias).all():
            c.slug = slugify(c.name)[:254]
            c.save()

    def unset_default_slug(apps, schema_editor):
        pass

    operations = [
        migrations.AddField(
            model_name="community",
            name="slug",
            field=models.SlugField(max_length=255, null=True, db_index=False),
        ),
        migrations.RunPython(set_default_slug, unset_default_slug),
        migrations.AlterField(
            model_name="community",
            name="slug",
            field=models.SlugField(unique=True, max_length=255),
        ),
    ]