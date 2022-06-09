from django.db import models

from users.models import Users


class Category(models.Model):
    """Сферы деятельности"""
    title = models.CharField(max_length=60, blank=True, null=True,
                             help_text="Категория помощи")


class Wallet(models.Model):
    """Кошелек пользователя"""
    # Лучше использовать связь OneToOneField
    user = models.OneToOneField(Users, on_delete=models.CASCADE,
                                null=True, blank=True)
    balance = models.PositiveBigIntegerField(default=100)


class Calendar(models.Model):
    """Календарь волонтера с текущими событиями"""
    #
    pass


"""
class History(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    """
