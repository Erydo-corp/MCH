from django.db import models


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
        verbose_name = "сферу"
        verbose_name_plural = "сфера"

    def __str__(self):
        return self.name


class Wallet(models.Model):
    """Кошелек пользователя"""
    user = models.OneToOneField(
        'users.Users',
        on_delete=models.CASCADE,
        verbose_name='волонтер'
    )
    balance = models.PositiveBigIntegerField('баланс', default=100)

    class Meta:
        verbose_name = "кошелек"
        verbose_name_plural = "кошелек"

    def __str__(self):
        return self.user


class Calendar(models.Model):
    """Календарь волонтера с текущими событиями"""
    pass


"""
class History(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
"""
