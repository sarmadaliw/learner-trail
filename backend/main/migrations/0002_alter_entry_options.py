# Generated by Django 5.0.1 on 2024-01-11 15:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="entry",
            options={"ordering": ["-created"], "verbose_name_plural": "entries"},
        ),
    ]
