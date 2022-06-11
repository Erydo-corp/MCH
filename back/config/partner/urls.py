from django.urls import path

from . import views

urlpatterns = [
    path('audience/', views.TargetAudienceView.as_view()),
    path('vacancys/', views.VacancyView.as_view()),
    path('projects/', views.ProjectView.as_view())
]
