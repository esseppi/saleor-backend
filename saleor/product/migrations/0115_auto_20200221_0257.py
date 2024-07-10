# Generated by Django 2.2.10 on 2020-02-21 08:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0114_auto_20200129_0815"),
    ]

    operations = [
        migrations.RenameField(
            model_name="attribute",
            old_name="meta",
            new_name="metadata",
        ),
        migrations.RenameField(
            model_name="attribute",
            old_name="private_meta",
            new_name="private_metadata",
        ),
        migrations.RenameField(
            model_name="category",
            old_name="meta",
            new_name="metadata",
        ),
        migrations.RenameField(
            model_name="category",
            old_name="private_meta",
            new_name="private_metadata",
        ),
        migrations.RenameField(
            model_name="collection",
            old_name="meta",
            new_name="metadata",
        ),
        migrations.RenameField(
            model_name="collection",
            old_name="private_meta",
            new_name="private_metadata",
        ),
        migrations.RenameField(
            model_name="digitalcontent",
            old_name="meta",
            new_name="metadata",
        ),
        migrations.RenameField(
            model_name="digitalcontent",
            old_name="private_meta",
            new_name="private_metadata",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="meta",
            new_name="metadata",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="private_meta",
            new_name="private_metadata",
        ),
        migrations.RenameField(
            model_name="producttype",
            old_name="meta",
            new_name="metadata",
        ),
        migrations.RenameField(
            model_name="producttype",
            old_name="private_meta",
            new_name="private_metadata",
        ),
        migrations.RenameField(
            model_name="productvariant",
            old_name="meta",
            new_name="metadata",
        ),
        migrations.RenameField(
            model_name="productvariant",
            old_name="private_meta",
            new_name="private_metadata",
        ),
    ]
