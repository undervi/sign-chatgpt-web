# Generated by Django 4.2.7 on 2023-12-06 03:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kakao_login", "0002_alter_users_gender_alter_users_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="profile_imeage_url",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
