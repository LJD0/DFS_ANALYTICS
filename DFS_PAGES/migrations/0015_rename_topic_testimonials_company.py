# Generated by Django 4.1.7 on 2024-03-12 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("DFS_PAGES", "0014_contact_forms_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="testimonials",
            old_name="topic",
            new_name="company",
        ),
    ]
