from django.urls import path
from . import views

app_name = "regions"

urlpatterns = [
    # path("<int:pk>", views.home_view, name="home"),
    path("도봉구/", views.show_data, name="도봉구"),
    path("동대문구/", views.show_data, name="동대문구"),
    path("용산구/", views.show_data, name="용산구"),
    path("동작구/", views.show_data, name="동작구"),
    path("은평구/", views.show_data, name="은평구"),
    path("강북구/", views.show_data, name="강북구"),
    path("강동구/", views.show_data, name="강동구"),
    path("강서구/", views.show_data, name="강서구"),
    path("금천구/", views.show_data, name="금천구"),
    path("구로구/", views.show_data, name="구로구"),
    path("관악구/", views.show_data, name="관악구"),
    path("광진구/", views.show_data, name="광진구"),
    path("강남구/", views.show_data, name="강남구"),
    path("종로구/", views.show_data, name="종로구"),
    path("중구/", views.show_data, name="중구"),
    path("중랑구/", views.show_data, name="중랑구"),
    path("마포구/", views.show_data, name="마포구"),
    path("노원구/", views.show_data, name="노원구"),
    path("서초구/", views.show_data, name="서초구"),
    path("서대문구/", views.show_data, name="서대문구"),
    path("성북구/", views.show_data, name="성북구"),
    path("성동구/", views.show_data, name="성동구"),
    path("송파구/", views.show_data, name="송파구"),
    path("양천구/", views.show_data, name="양천구"),
    path("영등포구/", views.show_data, name="영등포구"),
    path("타시도/", views.show_data, name="타시도"),
    path("기타/", views.show_data, name="기타"),
]
