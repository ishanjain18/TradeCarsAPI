import json
import urllib
import requests

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carApp.settings")
django.setup()

from car_site.models import *

# url = 'https://parseapi.back4app.com/classes/Car_Model_List?limit=10000&keys=Make'
# headers = {
#     'X-Parse-Application-Id': 'hlhoNKjOvEhqzcVAJ1lxjicJLZNVv36GdbboZj3Z', # This is the fake app's application id
#     'X-Parse-Master-Key': 'SNMJJF0CZZhTPhLDIqGhTlUNV9r60M2Z5spyWfXW' # This is the fake app's readonly master key
# }
# data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
# # print(json.dumps(data, indent=2))

# companies = []

# for i in data['results']:
#     companies.append(i['Make'])
# companies = sorted(set(companies))

# for company in companies:
#     a = Companies(name = company)
#     a.save()


# url = 'https://parseapi.back4app.com/classes/Car_Model_List?limit=5000&keys=Make,Model'
# headers = {
#     'X-Parse-Application-Id': 'hlhoNKjOvEhqzcVAJ1lxjicJLZNVv36GdbboZj3Z', # This is the fake app's application id
#     'X-Parse-Master-Key': 'SNMJJF0CZZhTPhLDIqGhTlUNV9r60M2Z5spyWfXW' # This is the fake app's readonly master key
# }
# data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
# # print(json.dumps(data, indent=2))

# cars = {}

# for i in data['results']:
#     if i['Model'] not in cars:
#         cars[i['Model']] = i['Make']

# for model in cars:
#     c = Cars(name = model, company = Companies.objects.get(name = cars[model]))
#     c.save()


data = {
    "make" : "BMW",
    "model_name": "8 Series",
    "seller_name" : "shalini",
    "seller_email": "vikas@example.com",
    "purchase_year": 2021,
    "min_price": 44.3,
    "max_price": 50.4 
}

# to avoid making multiple seller entries
# try:
#     seller_id = Sellers.objects.get(name=data["seller_name"])
# except:
#     seller = Sellers(name = data["seller_name"], email=data["seller_email"])
#     seller.save()
#     seller_id = Sellers.objects.get(name=data["seller_name"])


# make_id = Companies.objects.get(name=data['make'])
# model_id = Cars.objects.get(name=data['model_name'])
# year = data['purchase_year']
# lo = data['min_price']
# hi = data['max_price']

# listing = Listings(make=make_id, model_name=model_id, seller=seller_id, purchase_year=year, min_price=lo, max_price=hi)

# print(listing)
# print(listing.make)
# print(listing.model_name)
# print(listing.seller)
# print(listing.purchase_year)


listings = Listings.objects.filter(make=1).values()

print(listings)



# listing.save()