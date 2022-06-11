from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import TargetAudience, Vacancy, Project
from .serializers import TargetAudienceSerializers, VacancySerializers, ProjectSerializers


class TargetAudienceView(generics.ListAPIView):
    """Целевая аудитория список"""
    queryset = TargetAudience.objects.all()
    serializer_class = TargetAudienceSerializers


class VacancyView(generics.ListAPIView):
    """Вакансии"""
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializers


class ProjectView(generics.ListAPIView):
    """Проект компании"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers
