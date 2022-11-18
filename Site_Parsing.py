import requests
import json

Site = "https://www.kinopoisk.ru/s/type/film/list/1/m_act[year]/2022/"
r=requests.get("https://www.kinopoisk.ru/s/type/film/list/1/m_act[year]/2022/")

print(r)

print()