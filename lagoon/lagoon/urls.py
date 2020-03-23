"""lagoon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from backapp import permissions as custom_permissions
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from .api_urls import router

schema_view = get_schema_view(
    openapi.Info(
        title="Great API",
        default_version='v1',
        description="Great description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="beatuminflow@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticatedOrReadOnly, custom_permissions.IsOwnerOrReadOnly),
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth-user/', include('djoser.urls')),
    url(r'^api/v1/auth-token/', include('djoser.urls.authtoken')),
    url(r'^admin/', admin.site.urls),
]
