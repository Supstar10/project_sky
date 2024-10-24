# Generated by Django 5.1.1 on 2024-10-12 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0007_alter_blog_count_views_alter_blog_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="Version",
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
                ("product", models.TextField(max_length=100, verbose_name="продукт")),
                ("number", models.PositiveIntegerField(verbose_name="номер версии")),
                (
                    "name",
                    models.TextField(max_length=100, verbose_name="название версии"),
                ),
                (
                    "current_version",
                    models.BooleanField(
                        default=True, verbose_name="признак текущей версии"
                    ),
                ),
            ],
            options={
                "verbose_name": "Версия",
                "verbose_name_plural": "Версии",
            },
        ),
    ]
