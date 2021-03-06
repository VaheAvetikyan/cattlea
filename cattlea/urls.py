"""cattlea URL Configuration

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
from django.contrib import admin
from django.urls import re_path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^', include("cattlea.apps.core.urls")),
    re_path(r'^auth/', include("cattlea.apps.authentication.urls")),
    re_path(r'^carts/', include("cattlea.apps.carts.urls")),
    re_path(r'^orders/', include("cattlea.apps.orders.urls")),
    re_path(r'^i18n/', include('django.conf.urls.i18n')),
    re_path(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
