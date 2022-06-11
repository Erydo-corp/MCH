from django.db import models

from taggit.managers import TaggableManager

from volunteer.models import Direction
from users.models import Division, Users


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

    def get_absolute_url(self):
        pass


class Vacancy(models.Model):
    """Вакансии компании"""
    PARTICIPATION = (
        ('online', 'Онлайн'),
        ('offline', 'Офлайн'),
    )
    TYPE_OF_WORK = (
        ('without payment', 'Без оплаты'),
        ('permanent job', 'Постоянная'),
        ('internship', 'Стажировка'),
        ('side job', 'Подработка')
    )
    URGENCY = (
        ('urgently', 'Срочно'),
        ('not urgently', 'Не срочно'),
        ('within a week', 'В течение недели'),
        ('within a month', 'В течение месяца')
    )
    company_name = models.CharField('название компании', max_length=50)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, verbose_name='направление')
    type_of_work = models.CharField(
        'тип работы',
        max_length=50,
        choices=TYPE_OF_WORK,
        default='without payment',
    )
    name = models.CharField('наименование вакансии', max_length=100)
    terms = models.TextField('условия', max_length=100, help_text='Условия работы для волонтера')
    tasks = models.TextField('задачи', max_length=500, help_text='Описание задач для волонтера')
    description = models.TextField('описание', max_length=1000, help_text='Требования к кандидатам и функционал')
    salary = models.PositiveSmallIntegerField('заработная плата', blank=True, null=True)
    bonus = models.PositiveSmallIntegerField('размер бонусов', blank=True, null=True)
    motivation = models.TextField('мотивация волонтера', max_length=500,
                                  help_text='Описание мотивации волонтера', blank=True, null=True)
    target_audience = models.ForeignKey(
        TargetAudience,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='целевая аудитория',
    )
    publication_urgency = models.CharField('срочность публикации', max_length=30, choices=URGENCY, default='urgently')
    start_date = models.DateTimeField('начало мероприятия', help_text='Дата начала помощи', blank=True, null=True)
    end_data = models.DateTimeField('конец мероприятия', help_text='Дата завершения набора на вакансию', blank=True,
                                    null=True)
    allowable_age = models.CharField('возраст волонтера', blank=True, null=True, max_length=10,
                                     help_text='Подходящий возраст волонтера')
    mail_for_response = models.EmailField('эл.почта', help_text='E-mail для выгрузки откликов по вакансии')
    necessary_skills = TaggableManager('необходимые навыки')
    service = models.TextField('сервисы для волонтера', max_length=200,
                               help_text='Питание, экипировка, подтверждение опыта в ЛКВ')
    location = models.CharField('местоположение', max_length=100, help_text='Место проведения мероприятия')
    participation = models.CharField('способ участия', max_length=20, choices=PARTICIPATION)
    position = models.CharField('роль волонтера/должность', max_length=50, blank=True, null=True)
    division = models.OneToOneField(
        Division,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='административный округ'
    )
    users = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        verbose_name='компания',
        help_text='вакансия от партнера',
        blank=True,
        null=True
    )
    slug = models.SlugField('ссылка', max_length=200, unique=True)
    image = models.ImageField('картинка вакансии', upload_to='vacancy/')

    class Meta:
        verbose_name = "вакансию"
        verbose_name_plural = "вакансии"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass


class Project(models.Model):
    """Проект компаний"""
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

    def get_absolute_url(self):
        pass


class Response(models.Model):
    """
    Отклик
    Возможно понадобиться для выгрузки на Email
    """
    pass

# class Requirement(models.Model):
#     """Требования для вакансий"""
#     name = models.CharField('требование', max_length=15, blank=True, null=True)
#     description = models.TextField('описание', max_length=200, blank=True, null=True)
#     vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, blank=True, null=True)
#
#     class Meta:
#         verbose_name = "требования"
#         verbose_name_plural = "требование"
#
#     def __str__(self):
#         return self.name
