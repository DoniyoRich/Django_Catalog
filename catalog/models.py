from django.db import models


class Category(models.Model):
    """ Класс Категорий продукта. """
    name = models.CharField(
        max_length=150,
        verbose_name="Категория продукта"
    )
    description = models.TextField(
        verbose_name="Описание категории"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    """ Класс Продукта. """
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование продукта"
    )
    description = models.TextField(
        verbose_name="Описание продукта"
    )
    image = models.ImageField(
        upload_to="photos/products",
        verbose_name="Изображение",
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="products"
    )
    price = models.FloatField(
        verbose_name="Цена за покупку"
    )
    created_at = models.DateField(
        verbose_name="Дата создания", auto_now_add=True
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения", auto_now=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price", "created_at", "updated_at"]
