# -*- coding: utf-8 -*-
"""

"""
import json

city = '  budvA, me' # 3203106

def getCityIdFromName(name_cod):
    lst = name_cod.split(',')
    city = lst[0].strip().lower()
    cod = lst[1].strip().lower()
    with open('city.list.json','r', encoding='utf-8') as f:
        data = json.load(f)
    for item in data:
        if(cod != item['country'].lower()): continue
        if(city != item['name'].lower()): continue
        return item['id']
    return 0


print(getCityIdFromName(city))



"""
data.json
[
  {
    "id": 707860,
    "name": "Hurzuf",
    "country": "UA",
    "coord": {
      "lon": 34.283333,
      "lat": 44.549999
    }
  },
  {
    "id": 519188,
    "name": "Novinki",
    "country": "RU",
    "coord": {
      "lon": 37.666668,
      "lat": 55.683334
    }
  },

"""