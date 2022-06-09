from django.db import models

from volunteer.models import Category


class Vacancy(models.Model):
    """Вакансии организации"""
    name = models.CharField('название', max_length=50, blank=True, null=True)
    reward = models.PositiveSmallIntegerField('награда волонтера',
                                              help_text='количество баллов для волонтера',
                                              blank=True, null=True)
    slug = models.SlugField('ссылка', unique=True)
    description = models.TextField('описание', help_text="Описание вакансии", blank=True, null=True)
    data = models.DateTimeField('дата создания', auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='сфера', blank=True, null=True)
    users = models.ForeignKey(
        "users.Users",
        on_delete=models.CASCADE,
        verbose_name='волонтеры',
        blank=True,
        null=True
    )
    city = models.OneToOneField(
        "users.City",
        on_delete=models.CASCADE,
        verbose_name='город',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Вакансию"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass


class Project(models.Model):
    """Проекты организаций"""
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.PROTECT,
        help_text='История вакансий',
        verbose_name='вакансия',
        blank=True, null=True
    )
    name = models.CharField('название', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass


class Requirement(models.Model):
    """Требования для вакансий"""
    name = models.CharField('требование', max_length=15, blank=True, null=True)
    description = models.TextField('описание', max_length=200, blank=True, null=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Требования"
        verbose_name_plural = "Требовании"

    def __str__(self):
        return self.name
