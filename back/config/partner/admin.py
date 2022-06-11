from django.contrib import admin
from django.utils.safestring import mark_safe

from partner.models import Project, Vacancy, TargetAudience
from shop.models import Category, Product
from users.models import Users
from volunteer.models import Direction, Wallet


# Приложение партнеров
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Админка проекта"""
    # readonly_fields = ('get_image',)

    # нужна картинка проекта
    """
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.main_image.url} width="100" height="120"')

    get_image.short_description = 'Product image'
    """


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    """Админка вакансий"""
    prepopulated_fields = {'slug': ('name', 'company_name', 'direction',)}


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


# Приложение волонтера
@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    """Админка кошелька"""
    pass


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    """Админка сфер деятельности"""
    pass


@admin.register(TargetAudience)
class TargetAudience(admin.ModelAdmin):
    """Админка целевой аудитории"""
    pass


admin.site.site_header = "Сервис по размещению и поиску задач для волонтеров"
