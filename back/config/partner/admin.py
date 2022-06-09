from django.contrib import admin
from django.utils.safestring import mark_safe


from partner.models import Project, Vacancy
from shop.models import Section, Product
from users.models import Users
from volunteer.models import Category, Wallet
from .models import Project, Vacancy



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
    pass
