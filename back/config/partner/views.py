from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import TargetAudience, Vacancy, Project
from .serializers import TargetAudienceSerializers, VacancyListSerializers, \
    VacancyDetailSerializers, ProjectSerializers


class TargetAudienceView(generics.ListAPIView):
    """Целевая аудитория список"""
    queryset = TargetAudience.objects.all()
    serializer_class = TargetAudienceSerializers


class VacancyListView(generics.ListAPIView):
    """Список вакансий"""
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListSerializers
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('sphere', 'region', 'min_age', 'audience', 'is_paid_work', 'there_are_coins')


class VacancyDetailView(generics.RetrieveAPIView):
    """Вакансия подробно"""
    queryset = Vacancy.objects.all()
    serializer_class = VacancyDetailSerializers


class ProjectView(generics.ListAPIView):
    """Проект компании"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers
