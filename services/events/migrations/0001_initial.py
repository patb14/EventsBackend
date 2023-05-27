# Generated by Django 4.2.1 on 2023-05-27 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("name", models.CharField(max_length=256)),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField()),
                (
                    "location",
                    models.CharField(
                        choices=[
                            ("KRC", "KRC"),
                            ("CARDELL", "Cardell"),
                            ("SENSPLEX", "Sensplex"),
                        ],
                        max_length=32,
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("C", "Co-ed")],
                        max_length=6,
                    ),
                ),
                ("times", models.CharField(max_length=256)),
                ("cost", models.CharField(max_length=64)),
                ("created_timestamp", models.DateTimeField(auto_now_add=True)),
                ("last_updated_timestamp", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
