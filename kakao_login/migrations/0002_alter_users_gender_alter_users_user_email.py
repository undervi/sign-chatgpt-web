# Generated by Django 4.2.7 on 2023-12-05 03:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kakao_login", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="gender",
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name="users",
            name="user_email",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]