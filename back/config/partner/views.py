from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import TargetAudience, Vacancy, Project
from users.models import Users
from .serializers import TargetAudienceSerializers, VacancyListSerializers, \
    VacancyDetailSerializers, ProjectListSerializers, PartnerProfileSerializers, \
    ProjectDetailSerializers, RequirementListSerializers, BonusListSerializers


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
    def get(self, request, pk):
        queryset = Vacancy.objects.get(pk=pk)
        serializer_class = VacancyDetailSerializers(queryset, many=False)
        return Response(serializer_class.data)



class ProjectListView(generics.ListAPIView):
    """Проект компании"""
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializers


class ProjectDetailView(generics.RetrieveAPIView):
    """Проект компании"""
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializers


class PartnerProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Профиль партнера"""
    queryset = Users.objects.filter(is_partner=True)
    serializer_class = PartnerProfileSerializers


class RequirementListView(generics.ListAPIView):
    """Требования волонтера"""
    pass
