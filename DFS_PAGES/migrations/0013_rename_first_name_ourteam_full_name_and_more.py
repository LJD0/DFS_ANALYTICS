# Generated by Django 4.1.7 on 2024-03-09 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DFS_PAGES", "0012_features_growth_tab1_blurb4_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ourteam",
            old_name="first_name",
            new_name="full_name",
        ),
        migrations.RenameField(
            model_name="ourteam",
            old_name="facebook_link",
            new_name="linkedin_link",
        ),
        migrations.RemoveField(
            model_name="ourteam",
            name="instagram_link",
        ),
        migrations.RemoveField(
            model_name="ourteam",
            name="twitter_link",
        ),
        migrations.AddField(
            model_name="ourteam",
            name="blurb",
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name="ourteam",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]
