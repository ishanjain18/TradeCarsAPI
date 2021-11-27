from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
import json
        
def listings(request, **kwargs):
    
    listing_data = []
    companies = request.GET.get('companies')
    model = request.GET.get('model')
    year = request.GET.get('year')

    listings = Listings.objects.all()
    if companies:
        listings = listings.filter(make_id__in=companies.split(','))
    if model:
        listings = listings.filter(model_name_id__in=model.split(','))
    if year:
        listings = listings.filter(purchase_year__in=year.split(','))
    
    # sample API endpoint to fetch data -> http://127.0.0.1:8000/listings?companies=1,4,5&model=248,249&year=2002,2021
    
    for entry in listings.values():
        make_name = Companies.objects.get(pk=entry['make_id']).name
        car_name = Cars.objects.get(pk=entry['model_name_id']).name
        seller_obj = Sellers.objects.get(pk=entry['seller_id'])
        seller_name = seller_obj.name 
        seller_email = seller_obj.email
        purchase_year = entry['purchase_year']
        min_price = entry['min_price']
        max_price = entry['max_price']

        listing_data.append({
        'make_name' : make_name,
        'car_name' : car_name,
        'seller_name' : seller_name,
        'seller_email' : seller_email,
        'purchase_year' : purchase_year,
        'min_price' : min_price,
        'max_price' : max_price
        })

    data = {'results': listing_data}
    
    return JsonResponse(data)

def add_listing(request):

    
    if request.method == "POST":
        data = json.loads(request.body)
        # format of JSON data in POST request
        # data = {
        #         "make_name" : "Chrysler",
        #         "car_name": "Voyager",
        #         "seller_name" : "momo",
        #         "seller_email": "momo@example.com",
        #         "purchase_year": 2010,
        #         "min_price": 25.8,
        #         "max_price": 42.4 
        #       }

        # to avoid making multiple seller entries
        try:
            seller_id = Sellers.objects.get(name=data["seller_name"])
        except:
            seller = Sellers(name = data["seller_name"], email=data["seller_email"])
            seller.save()
            seller_id = Sellers.objects.get(name=data["seller_name"])


        make_id = Companies.objects.get(name=data['make_name'])
        model_id = Cars.objects.get(name=data['car_name'])
        year = data['purchase_year']
        lo = data['min_price']
        hi = data['max_price']

        listing = Listings(make=make_id, model_name=model_id, seller=seller_id, purchase_year=year, min_price=lo, max_price=hi)
        listing.save()

        return HttpResponse("Listing added successfully!")

    return HttpResponse("Invalid Request")