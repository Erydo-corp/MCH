from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Users(AbstractUser):
    """

    """
    # Волонтер
    age = models.PositiveSmallIntegerField(help_text="Возраст")
    education = models.CharField(max_length=25, help_text="Образование")
    phone = models.PositiveBigIntegerField(help_text="Телефон")
    discription = models.TextField(max_length=500,
                                   help_text="О себе, максимальная длинна 500 символов")
    photo = models.ImageField(upload_to="photo/", help_text="Фотография")

    # Партнер
    name = models.CharField(max_length=25, blank=True, help_text="Названии организации")
    is_partner = models.BooleanField(default=False)
    category = models.ForeignKey("volunteer.Category", on_delete=models.PROTECT,
                                 blank=True, null=True,
                                 help_text="Категория помощи")
