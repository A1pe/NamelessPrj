from django.shortcuts import render
from bs4 import BeautifulSoup
import os
import requests
from urllib.parse import urlencode, unquote
from datetime import date, timedelta


def get_data():
    get_number_url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13"
    res = requests.get(get_number_url)
    f_soup = BeautifulSoup(res.text, "html.parser")
    number = list(
        f_soup.find_all("td", {"class": "number", "headers": "status_level l_type1"})[1]
    )[0]

    KEY = os.environ.get("SERVICE_KEY")
    url = f"http://openapi.seoul.go.kr:8088/{KEY}/xml/Corona19Status/1/{number}/"
    req = requests.get(url)
    s_soup = BeautifulSoup(req.text, "html.parser")
    area = s_soup.find_all("corona19_area")
    area_list = []
    for i in area:
        area_list.append(i.string)
    dict_area = {region: area_list.count(region) for region in area_list}

    return dict_area


def show_data(request):
    pass
    return render(request, "regions/dobonggu.html")


def home_view(request):
    pass
    return render(request, "index.html")
