from django.db import models

from users.models import Users


class Category(models.Model):
    """Сферы деятельности"""
    title = models.CharField('название сферы', max_length=60, help_text="Категория помощи", blank=True, null=True)

    class Meta:
        verbose_name = "сферу деятельности"
        verbose_name_plural = "сферы деятельности"

    def __str__(self):
        return self.title


class Wallet(models.Model):
    """Кошелек пользователя"""
    # Лучше использовать связь OneToOneField
    user = models.OneToOneField(
        Users,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='волонтер'
    )
    balance = models.PositiveBigIntegerField('баланс', default=100)

    class Meta:
        verbose_name = "кошелек"
        verbose_name_plural = "кошельки"

    def __str__(self):
        return self.user


class Calendar(models.Model):
    """Календарь волонтера с текущими событиями"""
    pass


"""
class History(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
"""
