from rest_framework import generics

from .models import Sphere, Wallet
from .serializers import WalletSerializers, SphereSerializers


class WalletView(generics.ListAPIView):
    """Кошелек"""
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializers


class SphereView(generics.ListAPIView):
    """Направление (сфера деятельности)"""
    queryset = Sphere.objects.all()
    serializer_class = SphereSerializers
