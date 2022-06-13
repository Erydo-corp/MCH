from rest_framework import serializers

from .models import TargetAudience, Vacancy, Project, Task, Requirement, Bonus
from users.models import Users


class TaskSerializers(serializers.ModelSerializer):
    """Задачи"""

    class Meta:
        model = Task
        fields = '__all__'


class TargetAudienceSerializers(serializers.ModelSerializer):
    """Целевая аудитория"""

    class Meta:
        model = TargetAudience
        fields = '__all__'


class BonusListSerializers(serializers.ModelSerializer):
    """Бонусы волонтера(мотивация)"""

    class Meta:
        model = Bonus
        fields = '__all__'


class RequirementListSerializers(serializers.ModelSerializer):
    """Требования"""

    class Meta:
        model = Requirement
        fields = '__all__'


class VacancyListSerializers(serializers.ModelSerializer):
    """Вакансии список"""
    requirements = RequirementListSerializers()

    # requirements = serializers.RequirementListSerializers()

    # task = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        model = Vacancy
        fields = ['id', 'name', 'requirements']


class VacancyDetailSerializers(serializers.ModelSerializer):
    """Вакансия подробно"""
    sphere = serializers.SlugRelatedField(slug_field="name", read_only=True)

    # requirements = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    # bonus = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    # task = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    audience = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Vacancy
        fields = '__all__'


class ProjectListSerializers(serializers.ModelSerializer):
    """Вакансии"""

    class Meta:
        model = Project
        fields = '__all__'


class ProjectDetailSerializers(serializers.ModelSerializer):
    """Вакансии"""

    class Meta:
        model = Project
        fields = '__all__'


class PartnerProfileSerializers(serializers.ModelSerializer):
    """Профиль партнера"""

    class Meta:
        model = Users
        fields = '__all__'
