from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/volunteer/', include("volunteer.urls")),
    path('api/shop/', include("shop.urls")),
    path('api/partner/', include("partner.urls")),
    # path('users/', include("users.urls")),
    path('auth/', include("djoser.urls")),
    path('auth/', include("djoser.urls.authtoken")),
    path('auth/', include("djoser.urls.jwt")),
]

urlpatterns += doc_urls
