# Generated by Django 4.1.7 on 2024-03-09 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DFS_PAGES", "0011_testimonials_topic"),
    ]

    operations = [
        migrations.AddField(
            model_name="features",
            name="growth_tab1_blurb4",
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name="features",
            name="growth_tab1_title3",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="features",
            name="growth_tab2_blurb4",
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name="features",
            name="growth_tab2_title3",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]