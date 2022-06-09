from django.db import models
from volunteer.models import Category


class Vacancy(models.Model):
    """Вакансии организации"""
    name = models.CharField('название', max_length=50)
    reward = models.PositiveSmallIntegerField('награда волонтера',
                                              help_text='количество баллов для волонтера')
    slug = models.SlugField('ссылка', unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass


class Project(models.Model):
    """Проекты организаций"""
    vacancy = models.ManyToManyField(Vacancy, help_text='связь с таблицей вакансии')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField('название', max_length=100)
    photo = models.ImageField('фотография', upload_to='image/')
    data = models.DateTimeField('дата создания', auto_now_add=True)
    description = models.TextField('описание', max_length=500)
    slug = models.SlugField('ссылка', unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass


class Organization(models.Model):
    """Организация"""
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='projects',
        verbose_name='проект организации'
    )
    name = models.CharField('имя организации', max_length=100)
    unp = models.CharField('УНП', max_length=50, help_text='учётный номер плательщика')
    phone = models.CharField('номер телефона', max_length=30)
    email = models.EmailField('email')

    def __str__(self):
        return self.name
