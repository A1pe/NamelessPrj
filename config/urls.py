from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("dobonggu/", include("datas.urls", namespace="dobonggu")),
    path("admin/", admin.site.urls),
]
