# Generated by Django 4.1.7 on 2024-03-20 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DFS_PAGES", "0020_rename_contact_info_homepage_contact_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Features",
        ),
        migrations.AlterField(
            model_name="solutions_item",
            name="solutions_item_icon",
            field=models.FileField(upload_to=""),
        ),
    ]
