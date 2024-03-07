# Generated by Django 4.1.7 on 2024-03-07 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("DFS_PAGES", "0004_title_line_delete_title_lines"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pages",
            fields=[
                ("content", models.TextField()),
                ("button_text", models.CharField(max_length=100)),
                ("last_update", models.DateTimeField(auto_now=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("section", models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name="title_line",
            name="placement",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="title_lines",
                to="DFS_PAGES.pages",
            ),
        ),
        migrations.DeleteModel(
            name="Hero_Page",
        ),
    ]
