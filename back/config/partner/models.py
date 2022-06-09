from django.db import models

from volunteer.models import Category


class Vacancy(models.Model):
    """Вакансии организации"""
    name = models.CharField('название', max_length=50)
    reward = models.PositiveSmallIntegerField('награда волонтера',
                                              help_text='количество баллов для волонтера')
    slug = models.SlugField('ссылка', unique=True)
    discription = models.TextField(help_text="Описание вакансии")
    data = models.DateTimeField('дата создания', auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    users = models.ForeignKey("users.Users", on_delete=models.CASCADE)
    city = models.OneToOneField("users.City", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass


class Project(models.Model):
    """Проекты организаций"""
    vacancy = models.ForeignKey(Vacancy, on_delete=models.PROTECT,
                                help_text='История вакансий')
    name = models.CharField('название', max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass


class Requirement(models.Model):
    """Требования для вакансий"""
    name = models.CharField('требование', max_length=15)
    description = models.TextField('описание', max_length=200)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
