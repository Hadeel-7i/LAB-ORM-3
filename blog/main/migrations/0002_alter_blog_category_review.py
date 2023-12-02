# Generated by Django 4.2.7 on 2023-11-27 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="category",
            field=models.CharField(
                choices=[
                    ("Coffee", "Coffee"),
                    ("Tea", "Tea"),
                    ("Matcha", "Matcha"),
                    ("Water", "Water"),
                ],
                default="Coffee",
                max_length=2048,
            ),
        ),
        migrations.CreateModel(
            name="Review",
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
                ("full_name", models.CharField(max_length=512)),
                ("rating", models.FloatField()),
                ("comment", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "Blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.blog"
                    ),
                ),
            ],
        ),
    ]
