from django.contrib import admin
from django.utils.safestring import mark_safe


from partner.models import Project, Vacancy
from shop.models import Section, Product
from users.models import Users
from volunteer.models import Category, Wallet
from .models import Project, Vacancy



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
    prepopulated_fields = {'slug': ('name', 'category')}


# Приложение магазина
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админка товаров"""
    prepopulated_fields = {'slug': ('name', 'category')}
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="120"')

    get_image.short_description = 'Картинка продукта'


@admin.register(Section)
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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Админка сфер деятельности"""
    pass


admin.site.site_header = "Сервис по размещению и поиску задач для волонтеров"
