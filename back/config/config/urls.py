from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/volunteer/', include("volunteer.urls")),
    path('api/v1/shop/', include("shop.urls")),
    path('api/v1/partner/', include("partner.urls")),
    path('api/', include("volunteer.urls")),
    path('auth/', include("djoser.urls")),
    path('auth/', include("djoser.urls.authtoken")),
    path('auth/', include("djoser.urls.jwt")),
]
