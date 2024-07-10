# Generated by Django 3.2.20 on 2023-08-16 12:45

from django.contrib.postgres.indexes import BTreeIndex
from django.contrib.postgres.operations import AddIndexConcurrently
from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ("order", "0172_auto_20230627_0816"),
    ]

    operations = [
        AddIndexConcurrently(
            model_name="orderevent",
            index=BTreeIndex(
                fields=["related"], name="order_orderevent_related_id_idx"
            ),
        )
    ]
