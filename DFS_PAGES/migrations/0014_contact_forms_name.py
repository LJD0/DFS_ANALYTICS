# Generated by Django 4.2.3 on 2024-03-09 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DFS_PAGES", "0013_rename_first_name_ourteam_full_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact_forms",
            name="name",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
