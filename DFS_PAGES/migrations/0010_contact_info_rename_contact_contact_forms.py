# Generated by Django 4.1.7 on 2024-03-07 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DFS_PAGES", "0009_alter_aboutus_image_alter_features_growth_image_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact_Info",
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
                ("phone", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name="Contact",
            new_name="Contact_Forms",
        ),
    ]
