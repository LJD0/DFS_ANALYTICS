# Generated by Django 4.1.7 on 2024-03-19 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("DFS_PAGES", "0016_expo_form_expo_info"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomePage",
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
                ("last_update", models.DateTimeField(auto_now=True)),
                (
                    "about",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="aboutus",
                        to="DFS_PAGES.aboutus",
                    ),
                ),
                (
                    "contact_info",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contact_info",
                        to="DFS_PAGES.contact_info",
                    ),
                ),
                (
                    "faqs",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="faqs",
                        to="DFS_PAGES.faq",
                    ),
                ),
                (
                    "features",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="features",
                        to="DFS_PAGES.features",
                    ),
                ),
                (
                    "hero",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hero",
                        to="DFS_PAGES.hero",
                    ),
                ),
                (
                    "our_team",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="our_team",
                        to="DFS_PAGES.ourteam",
                    ),
                ),
                (
                    "testimonials",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="testimonials",
                        to="DFS_PAGES.testimonials",
                    ),
                ),
            ],
        ),
    ]