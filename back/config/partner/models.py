from django.db import models

from taggit.managers import TaggableManager

from volunteer.models import Sphere
from users.models import AdministrativeRegion, Users


class TargetAudience(models.Model):
    """Целевая аудитория"""
    name = models.CharField('название целевой аудитории', max_length=50,
                            help_text='высшее или среднее специальное образование')
    slug = models.SlugField('ссылка', max_length=200, unique=True)

    class Meta:
        verbose_name = "целевую аудиторию"
        verbose_name_plural = "целевые аудитории"

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    """Вакансии компании"""
    PARTICIPATION = (
        ('online', 'Онлайн'),
        ('offline', 'Офлайн'),
    )
    TYPE_OF_WORK = (
        ('without payment', 'Без оплаты'),
        ('full time', 'Постоянная'),
        ('internship', 'Стажировка'),
        ('side job', 'Подработка')
    )
    URGENT = (
        ('urgently', 'Срочно'),
        ('within a week', 'В течение недели'),
        ('within a month', 'В течение месяца')
    )

    # Информация от партнера
    company_name = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name='название компании',
        blank=True,
        null=True
    )
    sphere = models.ForeignKey(
        Sphere,
        on_delete=models.CASCADE,
        verbose_name='сфера деятельности'
    )
    name = models.CharField('наименование вакансии', max_length=100)
    type = models.CharField(
        'тип работы',
        max_length=50,
        choices=TYPE_OF_WORK,
        default='without payment',
    )
    start_date = models.DateTimeField('начало мероприятия', blank=True, null=True)
    end_data = models.DateTimeField('конец мероприятия', blank=True, null=True)
    salary = models.PositiveSmallIntegerField('заработная плата', blank=True, null=True)
    coins = models.PositiveSmallIntegerField('размер бонусов', blank=True, null=True)
    urgency = models.CharField('срочность публикации', max_length=30, choices=URGENT, default='urgently')
    location = models.CharField('местоположение', max_length=100, blank=True, null=True,
                                help_text='Место проведения мероприятия')
    email = models.EmailField('эл.почта', blank=True, null=True,
                              help_text='E-mail для выгрузки откликов')

    # Описание требуемого волонтера
    min_age = models.PositiveSmallIntegerField('минимальный возраст', blank=True, null=True)
    max_age = models.PositiveSmallIntegerField('максимальный возраст', blank=True, null=True)
    necessary_skills = TaggableManager('необходимые навыки')
    audience = models.ForeignKey(
        TargetAudience,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='целевая аудитория',
    )
    region = models.OneToOneField(
        AdministrativeRegion,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='административный округ'
    )
    slug = models.SlugField('ссылка', max_length=200, unique=True)

    class Meta:
        verbose_name = "вакансию"
        verbose_name_plural = "вакансии"

    def __str__(self):
        return self.name


class Project(models.Model):
    """Проекты компаний"""
    vacancy = models.ForeignKey(
        Vacancy,
        on_delete=models.PROTECT,
        help_text='история вакансий',
        verbose_name='вакансия',
        blank=True, null=True
    )
    name = models.CharField('название', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "проект"
        verbose_name_plural = "проекты"

    def __str__(self):
        return self.name


class HistoryResponse(models.Model):
    """История откликов"""
    volunteer = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "отклик"
        verbose_name_plural = "история откликов"


class Requirement(models.Model):
    """Требования для вакансий"""
    name = models.TextField('требование', max_length=200, blank=True, null=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "требования"
        verbose_name_plural = "требование"

    def __str__(self):
        return self.name


class Bonus(models.Model):
    """Список бонусов для волонтера"""
    name = models.TextField('задача', max_length=200, blank=True, null=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "бонусы"
        verbose_name_plural = "бонус"

    def __str__(self):
        return self.name


class Task(models.Model):
    """Список задач для волонтера"""
    name = models.TextField('задача', max_length=200, blank=True, null=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "задачи"
        verbose_name_plural = "задача"

    def __str__(self):
        return self.name
