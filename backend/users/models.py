from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from api.models import Stores

username_validator = RegexValidator(r'^[\w.@+-]+\Z')


class User(AbstractUser):
    """Модель пользователя."""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'position',
    ]
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
        verbose_name='Логин')
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Почта')
    shopping_mall = models.ForeignKey(
        Stores,
        on_delete=models.DO_NOTHING,
        verbose_name='ТК')
    position = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Должность')
    password = models.CharField(
        max_length=150,
        verbose_name='Пароль')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
