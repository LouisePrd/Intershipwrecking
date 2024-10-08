# Generated by Django 5.1 on 2024-09-02 18:33

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Application",
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
                ("company", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("applied_at", models.DateTimeField(auto_now_add=True)),
                ("type_of_application", models.CharField(max_length=200)),
                ("status", models.CharField(max_length=200)),
                ("link", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Candidate",
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
                ("username", models.CharField(max_length=20)),
                ("password", models.CharField(max_length=100)),
                ("mail", models.CharField(max_length=100)),
            ],
        ),
    ]
