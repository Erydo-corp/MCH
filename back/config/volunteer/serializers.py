from rest_framework import serializers

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
