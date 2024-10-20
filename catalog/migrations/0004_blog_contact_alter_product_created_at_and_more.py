# Generated by Django 5.1.1 on 2024-09-30 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_product_created_at_alter_product_updated_at"),
    ]

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
                ("heading", models.TextField(verbose_name="Заголовок")),
                ("slug", models.CharField(max_length=100, verbose_name="содержимое")),
                ("content", models.TextField(verbose_name="Содержимое")),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="img",
                        verbose_name="Фото товара",
                    ),
                ),
                (
                    "count_views",
                    models.IntegerField(verbose_name="количество просмотров"),
                ),
                (
                    "date_of_creation",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата создания"
                    ),
                ),
                (
                    "sing_of_publication",
                    models.BooleanField(
                        default=False, verbose_name="признак публикации"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=100, verbose_name="Имя")),
                (
                    "phone_number",
                    models.CharField(max_length=100, verbose_name="Номер телефона"),
                ),
                ("message", models.TextField(verbose_name="Сообщение")),
            ],
        ),
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateField(
                auto_now_add=True, verbose_name="Дата записи в базу данных"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="preview",
            field=models.ImageField(
                blank=True, null=True, upload_to="img", verbose_name="Фото товара"
            ),
        ),
    ]
