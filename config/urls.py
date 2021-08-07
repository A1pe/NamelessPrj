from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("regions/", include("datas.urls", namespace="regions")),
    path("admin/", admin.site.urls),
]
