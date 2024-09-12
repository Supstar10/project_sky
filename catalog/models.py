from django.db import models


class Product(models.Model):
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения в базе данных"
    )
    created_at = models.DateField(
        verbose_name="Дата записи в базу данных",
    )
    description = models.TextField(
        verbose_name="Описание товара",
        blank=True,
        null=True,
    )
    preview = models.ImageField(

        upload_to='catalog/photo',
        blank=True,
        null=True,
        verbose_name="Фото товара",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        verbose_name="Категория",
        help_text="Введите название категории",
        related_name="products",
        max_length=100,
    )
    price = models.IntegerField(
        verbose_name="Цена", help_text="Цена в рублях"
    )
    name = models.CharField(
        max_length=100, verbose_name="Название продукта", help_text="Выберите продукт"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "price"]


class Category(models.Model):
    description = models.TextField(
        verbose_name="Описание категории",
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Название категории",
        help_text="Выберите категорию",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
