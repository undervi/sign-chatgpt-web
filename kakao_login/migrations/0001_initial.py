# Generated by Django 4.2.7 on 2023-12-05 03:02

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "user_id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("user_name", models.CharField(max_length=50)),
                ("user_email", models.CharField(max_length=50)),
                ("gender", models.CharField(max_length=6)),
                ("profile_imeage_url", models.CharField(max_length=100)),
            ],
        ),
    ]
