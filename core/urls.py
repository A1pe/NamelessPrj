from django.urls import path
from datas import views as data_views

app_name = "core"

urlpatterns = [
    path("", data_views.home_view, name="home"),
    path("", data_views.get_data, name="home"),
]
