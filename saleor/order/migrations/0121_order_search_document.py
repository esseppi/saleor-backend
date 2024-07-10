# Generated by Django 3.2.6 on 2021-11-19 10:12
import django.contrib.postgres.indexes
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0120_orderline_optional_sku"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="search_document",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.RemoveIndex(
            model_name="order",
            name="order_order_user_em_bda05b_gin",
        ),
        migrations.AddIndex(
            model_name="order",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["search_document"],
                name="order_search_gin",
                opclasses=["gin_trgm_ops"],
            ),
        ),
        migrations.AddIndex(
            model_name="order",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["user_email"],
                name="order_email_search_gin",
                opclasses=["gin_trgm_ops"],
            ),
        ),
    ]
