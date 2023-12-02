# Generated by Django 4.2.7 on 2023-11-26 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("name", models.CharField(max_length=512)),
                ("paragraph", models.TextField(default="--")),
                ("release_date", models.DateField(auto_now=True)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Coffee", "Coffee"),
                            ("Tea", "Tea"),
                            ("Matcha", "Matcha"),
                            ("water", "Water"),
                        ],
                        default="Coffee",
                        max_length=2048,
                    ),
                ),
                (
                    "image",
                    models.ImageField(default="image/default.jpg", upload_to="image/"),
                ),
            ],
        ),
    ]
