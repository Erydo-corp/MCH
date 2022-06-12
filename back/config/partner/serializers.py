from rest_framework import serializers

from .models import TargetAudience, Vacancy, Project, \
    HistoryResponse, Requirement, Bonus, Task


class TargetAudienceSerializers(serializers.ModelSerializer):
    """Целевая аудитория"""

    class Meta:
        model = TargetAudience
        fields = '__all__'


class VacancyListSerializers(serializers.ModelSerializer):
    """Вакансии список"""
    task = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        model = Vacancy
        fields = ['id', 'name', 'task']


class VacancyDetailSerializers(serializers.ModelSerializer):
    """Вакансия подробно"""
    sphere = serializers.SlugRelatedField(slug_field="name", read_only=True)
    requirements = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    bonus = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    task = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    audience = serializers.SlugRelatedField(slug_field="name", read_only=True)

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
