from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    phone = models.CharField(max_length=35, verbose_name="Телефон", **NULLABLE, help_text="ВВедите номер телефона")
    avatar = models.ImageField(upload_to='users/avatar/', **NULLABLE, verbose_name='Аватар')
    country = models.CharField(max_length=35, verbose_name='Страна', **NULLABLE)

    token = models.CharField(max_length=100, verbose_name="Токен", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
