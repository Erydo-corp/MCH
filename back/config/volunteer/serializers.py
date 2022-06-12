from rest_framework import serializers

from users.models import Users
from .models import Sphere, Wallet


class WalletSerializers(serializers.ModelSerializer):
    """Кошелек волонтера"""

    class Meta:
        model = Wallet
        fields = "__all__"


class SphereSerializers(serializers.ModelSerializer):
    """Направление (сфера деятельности)"""

    class Meta:
        model = Sphere
        fields = "__all__"


class VolunteerProfileSerializers(serializers.ModelSerializer):
    """Профиль волонтера"""

    class Meta:
        model = Users
        fields = "__all__"
