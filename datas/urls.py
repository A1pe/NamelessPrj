from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("<int:pk>", views.home_view, name="home"),
    path("dobonggu/", views.show_data, name="show"),
]
