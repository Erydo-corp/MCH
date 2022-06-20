from django.urls import path

from . import views

urlpatterns = [
    path('audience/', views.TargetAudienceView.as_view()),
    path('vacancys/', views.VacancyListView.as_view()),
    path('vacancys/<int:pk>/', views.VacancyDetailView.as_view()),
    path('projects/', views.ProjectListView.as_view()),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view()),
    path('profile/<int:pk>/', views.PartnerProfileDetailView.as_view()),
]
