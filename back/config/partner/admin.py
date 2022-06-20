from django.contrib import admin
from django.utils.safestring import mark_safe

from partner.models import Project, Vacancy, TargetAudience, \
    HistoryResponse, Requirement, Bonus, Task, NecessarySkill
from shop.models import Category, Product
from users.models import Users, AdministrativeRegion
from volunteer.models import Sphere, Wallet


# Приложение партнера
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Админка проекта"""
    pass


@admin.register(NecessarySkill)
class NecessarySkillAdmin(admin.ModelAdmin):
    """Админка проекта"""
    pass


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    """Админка вакансий"""
    prepopulated_fields = {'slug': ('name', 'sphere',)}


@admin.register(HistoryResponse)
class HistoryResponseAdmin(admin.ModelAdmin):
    """История откликов"""
    pass


@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    """Требования"""
    pass


@admin.register(Bonus)
class BonusAdmin(admin.ModelAdmin):
    """Бонусы"""
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Задачи"""
    pass


# Приложение магазина
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админка товаров"""
    prepopulated_fields = {'slug': ('name', 'category')}
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="120"')

    get_image.short_description = 'Картинка продукта'


@admin.register(Category)
class SectionAdmin(admin.ModelAdmin):
    """Админка категорий магазина"""
    prepopulated_fields = {'slug': ('name',)}


# Пользователь
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    """Админка пользователя"""
    pass


@admin.register(AdministrativeRegion)
class AdminRegionAdmin(admin.ModelAdmin):
    """Административный округ"""
    pass


# Приложение волонтера
@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    """Админка кошелька"""
    pass


@admin.register(Sphere)
class DirectionAdmin(admin.ModelAdmin):
    """Админка сфер деятельности"""
    pass


@admin.register(TargetAudience)
class TargetAudience(admin.ModelAdmin):
    """Админка целевой аудитории"""
    prepopulated_fields = {'slug': ('name',)}


admin.site.site_header = "Сервис по размещению и поиску задач для волонтеров"


