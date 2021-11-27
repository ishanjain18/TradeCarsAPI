from django.urls import path
from . import views

# Used to map URL endpoints to view functions

urlpatterns = [
    # shows all listings
    path("listings", views.listings),
    path("listings/add", views.add_listing)    

]