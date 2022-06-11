from django.db import models

from users.models import Users


class Sphere(models.Model):
    """Направление деятельности"""
    name = models.CharField(
        'направление',
        max_length=60,
        help_text="направление помощи",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "сфера деятельности"
        verbose_name_plural = "сферу деятельности"

    def __str__(self):
        return self.name


class Wallet(models.Model):
    """Кошелек пользователя"""
    user = models.OneToOneField(
        Users,
        on_delete=models.CASCADE,
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
