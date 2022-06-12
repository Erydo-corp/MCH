from rest_framework import generics

from .models import Sphere, Wallet
from users.models import Users
from .serializers import WalletSerializers, SphereSerializers, VolunteerProfileSerializers


class WalletView(generics.ListAPIView):
    """Кошелек"""
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializers


class SphereView(generics.ListAPIView):
    """Направление (сфера деятельности)"""
    queryset = Sphere.objects.all()
    serializer_class = SphereSerializers


class VolunteerProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Профиль волонтера"""
    queryset = Users.objects.filter(is_partner=False)
    serializer_class = VolunteerProfileSerializers
