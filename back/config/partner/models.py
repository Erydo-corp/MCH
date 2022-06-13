from django.db import models

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


class NecessarySkill(models.Model):
    """Необходимые навыки"""
    name = models.TextField('необходимый навык', max_length=50)

    class Meta:
        verbose_name = "навыки"
        verbose_name_plural = 'навык'

    def __str__(self):
        return self.name


class TypeWork(models.Model):
    """Тип работы"""
    name = models.CharField('тип работы', max_length=30, help_text='Полный день/Сменный график/Гибкий график')

    class Meta:
        verbose_name = "тип работы"
        verbose_name_plural = 'тип работы'

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    """Вакансии компании"""
    PARTICIPATION = (
        ('online', 'Онлайн'),
        ('offline', 'Офлайн'),
    )
    URGENT = (
        ('urgently', 'Срочно'),
        ('in a week', 'В течение недели'),
        ('in a month', 'В течение месяца')
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
        'volunteer.Sphere',
        on_delete=models.CASCADE,
        verbose_name='сфера деятельности'
    )
    name = models.CharField('наименование вакансии', max_length=100)
    type = models.ForeignKey(TypeWork, on_delete=models.CASCADE, verbose_name='тип работы', blank=True, null=True)
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
    key_skills = models.ManyToManyField(NecessarySkill, verbose_name='необходимые навыки')

    # Целевая группа
    audience = models.ForeignKey(
        TargetAudience,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='целевая аудитория',
    )

    # Административный округ
    region = models.ForeignKey(
        AdministrativeRegion,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='административный округ'
    )

    slug = models.SlugField('ссылка', max_length=200, unique=True)

    # Для фильтров
    is_paid_work = models.BooleanField('за работу платят рублями', default=False)
    there_are_coins = models.BooleanField('есть бонусы для магазина', default=False)

    class Meta:
        verbose_name = "вакансию"
        verbose_name_plural = "вакансии"

    def __str__(self):
        return self.name


class Requirement(models.Model):
    """Требования для вакансий"""
    name = models.CharField('название', max_length=15, blank=True, null=True)
    description = models.TextField('требование', max_length=200, blank=True, null=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, blank=True, null=True, verbose_name='вакансия')

    class Meta:
        verbose_name = "Требования"
        verbose_name_plural = "Требовании"

    def __str__(self):
        return self.name


class Bonus(models.Model):
    """Список бонусов для волонтера"""
    name = models.TextField('название', max_length=200, blank=True, null=True)
    description = models.TextField('бонус', max_length=200, blank=True, null=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, blank=True, null=True, verbose_name='вакансия')

    class Meta:
        verbose_name = "бонусы"
        verbose_name_plural = "бонус"

    def __str__(self):
        return self.name


class Task(models.Model):
    """Список задач для волонтера"""
    name = models.TextField('задача', max_length=200, blank=True, null=True)
    description = models.TextField('описание', max_length=200, blank=True, null=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, blank=True, null=True, verbose_name='вакансия')

    class Meta:
        verbose_name = "задача"
        verbose_name_plural = "задачи"

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

    def __str__(self):
        return self.volunteer
