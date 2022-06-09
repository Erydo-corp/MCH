from django.db import models
from users.models import Users


class Category(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True,
                             help_text="Категория помощи")


class Wallet(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE,
                             primary_key=True)
    balance = models.PositiveBigIntegerField(default=100)

"""
class History(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    """



