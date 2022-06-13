from django.urls import path

from . import views

urlpatterns = [
    path('wallets/', views.WalletView.as_view()),
    path('directions/', views.SphereView.as_view()),
    path('profile/<int:pk>/', views.VolunteerProfileDetailView.as_view()),
]
