# Generated by Django 4.2.16 on 2024-10-17 11:36

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(max_length=250)),
                ("email", models.CharField(max_length=150)),
                ("phone", models.CharField(max_length=20)),
            ],
            options={
                "verbose_name": "Contact",
                "verbose_name_plural": "Contact",
            },
        ),
    ]
