from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    """Модель пользователя"""
    # Волонтер
    age = models.PositiveSmallIntegerField('возраст', help_text="Возраст", null=True, blank=True)
    education = models.CharField('образование', max_length=25, help_text="Образование", blank=True, null=True)
    phone = models.PositiveBigIntegerField('телефон', help_text="Телефон", null=True, blank=True)
    description = models.TextField('о себе', max_length=500,
                                   help_text="О себе, максимальная длинна 500 символов", blank=True, null=True)
    photo = models.ImageField('фотография', upload_to="photo/", help_text="Фотография", blank=True, null=True)
    # city

    # Партнер
    name = models.CharField('имя партнера', max_length=25, blank=True, null=True, help_text="Названии организации")
    is_partner = models.BooleanField('это партнер', default=False)
    category = models.ForeignKey(
        "volunteer.Category",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        help_text="Категория помощи",
        verbose_name='сфера деятельности'
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.name


class City(models.Model):
    """Город"""
    name = models.CharField(max_length=50, blank=True, null=True)
    users = models.ForeignKey(
        Users,
        verbose_name='Пользователь',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )

    verbose_name = "Город"
    verbose_name_plural = "Города"

    def __str__(self):
        return self.name


"""
Для открытия поля с опытом при регистрации волонтера 
    STATUS_CHOICES = (
        ('no', 'Нет опыта'),
        ('yes', 'Есть опыт'),
    )
    experience = models.CharField('Опыт', max_length=15, choices=STATUS_CHOICES)
"""
