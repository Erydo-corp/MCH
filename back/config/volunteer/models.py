from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=60, blank=True, null=True,
                             help_text="Категория помощи")


class Wallet(models.Model):
