# Generated by Django 4.1.7 on 2024-03-08 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DFS_PAGES", "0010_contact_info_rename_contact_contact_forms"),
    ]

    operations = [
        migrations.AddField(
            model_name="testimonials",
            name="topic",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
