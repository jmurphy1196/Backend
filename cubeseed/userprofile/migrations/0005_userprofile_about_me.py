# Generated by Django 4.2.1 on 2023-07-06 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0004_rename_userprofile_userprofilephoto_user_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="about_me",
            field=models.TextField(blank=True),
        ),
    ]