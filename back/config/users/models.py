from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    """Модель абстрактного пользователя"""
    # Волонтер
    age = models.PositiveSmallIntegerField(help_text="Возраст", null=True, blank=True)
    education = models.CharField(max_length=25, help_text="Образование")
    phone = models.PositiveBigIntegerField(help_text="Телефон", null=True, blank=True)
    description = models.TextField(max_length=500,
                                   help_text="О себе, максимальная длинна 500 символов")
    photo = models.ImageField(upload_to="photo/", help_text="Фотография")
    # city

    # Партнер
    name = models.CharField(max_length=25, blank=True, help_text="Названии организации")
    is_partner = models.BooleanField(default=False)
    category = models.ForeignKey("volunteer.Category", on_delete=models.PROTECT,
                                 blank=True, null=True,
                                 help_text="Категория помощи")



class City(models.Model):
    name = models.CharField(max_length=50)
    users = models.ForeignKey(Users, on_delete=models.PROTECT)



"""
Для открытия поля с опытом при регистрации волонтера 
    STATUS_CHOICES = (
        ('no', 'Нет опыта'),
        ('yes', 'Есть опыт'),
    )
    experience = models.CharField('Опыт', max_length=15, choices=STATUS_CHOICES)
"""
