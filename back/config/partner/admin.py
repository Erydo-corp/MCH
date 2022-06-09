from django.contrib import admin

from .models import Project, Vacancy



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    pass
