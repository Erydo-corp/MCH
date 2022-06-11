from django.urls import path

from . import views

urlpatterns = [
    path('wallets/', views.WalletView.as_view()),
    path('directions/', views.SphereView.as_view()),
]
