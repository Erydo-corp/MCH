from rest_framework import serializers

from .models import TargetAudience, Vacancy, Project, \
    HistoryResponse, Requirement, Bonus, Task


class TargetAudienceSerializers(serializers.ModelSerializer):
    """Целевая аудитория"""

    class Meta:
        model = TargetAudience
        fields = '__all__'


class VacancySerializers(serializers.ModelSerializer):
    """Вакансии"""

    class Meta:
        model = Vacancy
        fields = '__all__'


class ProjectSerializers(serializers.ModelSerializer):
    """Вакансии"""

    class Meta:
        model = Project
        fields = '__all__'


# class ProjectSerializers(serializers.ModelSerializer):
#     """Вакансии"""
#
#     class Meta:
#         model = Project
#         fields = '__all__'
#
#
# class ProjectSerializers(serializers.ModelSerializer):
#     """Вакансии"""
#
#     class Meta:
#         model = Project
#         fields = '__all__'
#
#
# class ProjectSerializers(serializers.ModelSerializer):
#     """Вакансии"""
#
#     class Meta:
#         model = Project
#         fields = '__all__'
#
#
# class ProjectSerializers(serializers.ModelSerializer):
#     """Вакансии"""
#
#     class Meta:
#         model = Project
#         fields = '__all__'
