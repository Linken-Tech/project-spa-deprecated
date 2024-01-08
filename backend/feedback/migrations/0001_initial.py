# Generated by Django 4.1.2 on 2023-04-23 10:45

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Feedback",
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
                ("user_email", models.EmailField(max_length=254)),
                ("feedback_title", models.CharField(max_length=50)),
                ("feedback_detail", models.CharField(max_length=255)),
                ("feedback_status", models.BooleanField(default="False")),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
